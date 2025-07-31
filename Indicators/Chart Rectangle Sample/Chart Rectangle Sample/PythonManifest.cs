using System;

namespace cAlgo.Indicators;

public class PythonManifest
{
    public string RootNamespace { get; set; } = string.Empty;
    public string[] PythonFiles { get; set; } = Array.Empty<string>();
}