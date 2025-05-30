using System;
using System.IO;
using System.Linq;

namespace cAlgo.Robots;

internal class EngineHelper
{
    internal static string CreatePythonFolder()
    {
        var pyScriptsDirectory = new DirectoryInfo(Path.Combine("py_scripts"));
        if (!pyScriptsDirectory.Exists)
            pyScriptsDirectory.Create();

        return pyScriptsDirectory.FullName;
    }

    internal static void CopyPythonResources(string pythonFolder)
    {
        var pythonResources = EmbeddedResourceProvider.List()
            .Where(res => res.ToLower().EndsWith(".py"))
            .ToList();

        foreach (var resource in pythonResources)
        {
            var firstDot = resource.IndexOf('.');
            if (firstDot <= 0)
                continue;

            var pathWithoutNamespace = resource[(firstDot + 1)..];
            var lastDot = pathWithoutNamespace.LastIndexOf('.');
            if (lastDot <= 0)
                continue;

            var extension = pathWithoutNamespace[lastDot..];
            var pathWithoutExtension = pathWithoutNamespace[..lastDot];
            var directoryPath =
                Path.Combine(pythonFolder, pathWithoutExtension.Replace('.', Path.DirectorySeparatorChar));
            var filePath = directoryPath + extension;
            var directory = Path.GetDirectoryName(filePath);

            if (!string.IsNullOrEmpty(directory) && !Directory.Exists(directory))
                Directory.CreateDirectory(directory);

            using (var stream = EmbeddedResourceProvider.ReadStream(resource))
            using (var fileStream = File.Create(filePath))
                stream.CopyTo(fileStream);
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
