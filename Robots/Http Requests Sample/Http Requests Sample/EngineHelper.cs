using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using cAlgo.API.Internals;
using Python.Runtime;

namespace cAlgo.Robots;

internal static class EngineHelper
{
    private static Dictionary<string, string> _moduleCodeMap = new();

    public static void Initialize(Algo algo)
    {
        InjectPrintDelegate(algo.Print);
        InitializePythonCodeModuleMap(algo);
        SetApiGlobal(algo);
    }

    private static void InitializePythonCodeModuleMap(Algo algo)
    {
        _moduleCodeMap = new Dictionary<string, string>();

        CopyPythonResources((fileName, resourceName) =>
        {
            using var stream = EmbeddedResourceProvider.ReadStream(resourceName);
            using var reader = new StreamReader(stream);
            var moduleName = Path.GetFileNameWithoutExtension(fileName);
            var pyCode = reader.ReadToEnd();
            _moduleCodeMap[moduleName] = pyCode;
        });

        _moduleCodeMap["traceback"] = PythonHooks.DummyTraceback;
        SetupPythonSourceCodeModulesInMemory();
    }

    private static void SetupPythonSourceCodeModulesInMemory()
    {
        using (Py.GIL())
        {
            dynamic main = Py.Import("__main__");
            PyObject mainDict = main.GetAttr("__dict__");
            PythonEngine.Exec(PythonHooks.InMemoryModuleLoaderPythonCode, mainDict.As<PyDict>());

            using var pyDict = new PyDict();
            foreach (var kv in _moduleCodeMap)
                pyDict[new PyString(kv.Key)] = new PyString(kv.Value);

            main.install_inmemory_importer(pyDict, false);
        }
    }

    private static void SetApiGlobal(Algo algo)
    {
        using (Py.GIL())
        {
            PythonEngine.Exec(@"
import builtins

builtins.api = None
");

            dynamic builtinsModule = Py.Import("builtins");
            builtinsModule.api = algo.ToPython();
        }
    }

    public static void InjectPrintDelegate(Action<object[]> printer)
    {
        using (Py.GIL())
        {
            dynamic builtins = Py.Import("builtins");
            builtins.__setattr__("cs_print", new Action<PyObject[]>(printer).ToPython());
            PythonEngine.Exec(@"
import builtins

def py_print(*args):
    builtins.cs_print(args)

builtins.print = py_print
");
        }
    }

    internal static void CopyPythonResources(Action<string, string> readFileAction)
    {
        if (!EmbeddedResourceProvider.TryGetPythonManifest(out var pythonManifest))
            throw new Exception("Python manifest not found");

        var resourceNameAndPaths = new Dictionary<string, FileInfo>();

        foreach (var pythonFile in pythonManifest.PythonFiles)
        {
            var pythonFileInfo = new FileInfo(pythonFile.Replace('/', Path.DirectorySeparatorChar));
            var resourceName = PathToResourceName(pythonFile);
            resourceNameAndPaths[$"{pythonManifest.RootNamespace}.{resourceName}"] = pythonFileInfo;
        }

        var pythonResources = EmbeddedResourceProvider.List()
            .Where(res => res.ToLower().EndsWith(".py"))
            .ToList();

        foreach (var pythonResource in pythonResources)
        {
            if (!resourceNameAndPaths.TryGetValue(pythonResource, out var fileInfo))
                throw new Exception($"Python resource '{pythonResource}' not found in python manifest");

            readFileAction(fileInfo.FullName, pythonResource);
        }
    }

    internal static string GetClassName(string code)
    {
        return code.Split("class", StringSplitOptions.TrimEntries | StringSplitOptions.RemoveEmptyEntries)
            .Skip(1).FirstOrDefault()
            ?.Split('(', StringSplitOptions.TrimEntries | StringSplitOptions.RemoveEmptyEntries).FirstOrDefault()
            ?.Trim();
    }

    private static string PathToResourceName(string path)
    {
        var directoryName = Path.GetDirectoryName(path);
        var fileName = Path.GetFileName(path);

        if (string.IsNullOrEmpty(directoryName))
            return path;

        if (string.IsNullOrEmpty(fileName))
            return path;

        var invalidChars = new[] { ' ', ';', '!', '@', '#', '$', '%', '^', '&', '(', ')', '+', '-', '\'', '=', '`', '~', '[', ']', '{', '}' };
        directoryName = invalidChars
            .Aggregate(directoryName, (current, c) => current.Replace(c.ToString(), "_"))
            .Replace('/', '.');

        return directoryName + "." + fileName;
    }
}