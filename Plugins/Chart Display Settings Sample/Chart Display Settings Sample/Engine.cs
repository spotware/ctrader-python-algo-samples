using System;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Plugins;

public partial class ChartDisplaySettingsSample : Plugin
{
    private PluginBridge _plugin;
    private const string MainPythonFile = "Chart Display Settings Sample_main.py";

    protected override void OnStart()
    {
        EngineHelper.Initialize(this, Print);

        using (Py.GIL())
        {
            var code = EmbeddedResourceProvider.ReadText(MainPythonFile);
            var className = EngineHelper.GetClassName(code);

            using (var scope = Py.CreateScope())
            {
                scope.Set("currentAssembly", System.Reflection.Assembly.GetExecutingAssembly());

                try
                {
                    scope.Exec(code);
                    if (!scope.Contains(className))
                    {
                        Print($"Error: Python class '{className}' not found in the module!");
                        throw new InvalidOperationException($"Python class '{className}' not found in the module");
                    }

                    dynamic pythonClass = scope.Get(className);
                    _plugin = new PluginBridge(pythonClass());

                    _plugin.OnStart();
                }
                catch (Exception ex)
                {
                    Print($"Error initializing Python: {ex.Message}\nStack trace: {ex.StackTrace}");
                    throw;
                }
            }
        }
    }

    protected override void OnStop()
    {
        using (Py.GIL())
            _plugin.OnStop();
    }
}