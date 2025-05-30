using System;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Plugins;

[Plugin(AccessRights = AccessRights.None)]
public class TestPlugin : Plugin
{
    private dynamic _plugin;
    private const string MainPythonFile = "TestPlugin.py";

    protected override void OnStart()
    {
        using (Py.GIL())
        {
            var pythonFolder = EngineHelper.CreatePythonFolder();
            EngineHelper.CopyPythonResources(pythonFolder);

            dynamic sys = Py.Import("sys");
            sys.path.append(pythonFolder);

            var code = EmbeddedResourceProvider.ReadText(MainPythonFile);
            var className = EngineHelper.GetClassName(code);

            using (var scope = Py.CreateScope())
            {
                scope.Set("api", this);
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
                    _plugin = pythonClass();

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