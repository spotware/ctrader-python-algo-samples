using System;
using System.IO;
using System.Linq;
using System.Text.Json;

namespace cAlgo.Plugins;

internal class EmbeddedResourceProvider
{
    public const string PythonManifestFileName = "EmbeddedResources.manifest.json";

    internal static string[] List()
    {
        var assembly = typeof(EmbeddedResourceProvider).Assembly;
        return assembly.GetManifestResourceNames();
    }

    internal static string ReadText(string name)
    {
        var assembly = typeof(EmbeddedResourceProvider).Assembly;
        var resourceName = assembly.GetManifestResourceNames()
            .SingleOrDefault(n => n.EndsWith($".{name}", StringComparison.OrdinalIgnoreCase));

        if (resourceName == null)
            return null;

        using var stream = assembly.GetManifestResourceStream(resourceName);
        if (stream == null)
            return null;

        using var stringReader = new StreamReader(stream);
        return stringReader.ReadToEnd();
    }

    internal static Stream ReadStream(string name)
    {
        var assembly = typeof(EmbeddedResourceProvider).Assembly;
        return assembly.GetManifestResourceStream(name);
    }

    public static bool TryGetPythonManifest(out PythonManifest pythonManifest)
    {
        pythonManifest = null;
        var pythonManifestJson = ReadText(PythonManifestFileName);

        if (string.IsNullOrEmpty(pythonManifestJson))
            return false;
        
        pythonManifest = JsonSerializer.Deserialize<PythonManifest>(pythonManifestJson);

        return true;
    }
}