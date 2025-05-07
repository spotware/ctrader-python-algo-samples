using System.IO;

namespace cAlgo.Plugins;

internal class EmbeddedResourceProvider
{
    internal static string[] List()
    {
        var assembly = typeof(EmbeddedResourceProvider).Assembly;
        return assembly.GetManifestResourceNames();
    }

    internal static string ReadText(string name)
    {
        var assembly = typeof(EmbeddedResourceProvider).Assembly;
        using var stream = assembly.GetManifestResourceStream(name);
        if (stream == null)
            return null;

        using var stringReader = new StreamReader(stream);
        return stringReader.ReadToEnd();
    }
}
