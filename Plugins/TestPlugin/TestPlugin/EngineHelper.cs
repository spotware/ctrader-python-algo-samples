using System;
using System.IO;
using System.Linq;

namespace cAlgo.Plugins;

internal class EngineHelper
{
    internal static string CreatePythonFolder()
    {
        var pyScriptsDirectory = new DirectoryInfo(Path.Combine("py_scripts"));
        if (!pyScriptsDirectory.Exists)
            pyScriptsDirectory.Create();

        return pyScriptsDirectory.FullName;
    }

    internal static void CopyPythonResources(string pythonFolder, string mainPythonFile, string algoName)
    {
        var pythonResources = EmbeddedResourceProvider.List()
            .Where(res => res.ToLower().EndsWith(".py") && !res.Equals(mainPythonFile, StringComparison.OrdinalIgnoreCase))
            .ToList();

        foreach (var pythonResource in pythonResources)
        {
            var pythonCode = EmbeddedResourceProvider.ReadText(pythonResource);
            File.WriteAllText(Path.Combine(pythonFolder, pythonResource.Replace($"{algoName}.", "")), pythonCode);
        }
    }

    internal static string GetClassName(string code)
    {
        return code.Split("class", StringSplitOptions.TrimEntries | StringSplitOptions.RemoveEmptyEntries)
            .Skip(1).FirstOrDefault()
            ?.Split('(', StringSplitOptions.TrimEntries | StringSplitOptions.RemoveEmptyEntries).FirstOrDefault()
            ?.Trim();
    }
}
