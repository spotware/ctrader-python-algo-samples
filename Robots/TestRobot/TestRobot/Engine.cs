using System;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public class TestRobot : Robot
{
    private dynamic _robot;
    private const string MainPythonFile = "TestRobot.py";

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
                    _robot = pythonClass();

                    _robot.OnStart();
                }
                catch (Exception ex)
                {
                    Print($"Error initializing Python: {ex.Message}\nStack trace: {ex.StackTrace}");
                    throw;
                }
            }
        }
    }

    protected override void OnTick()
    {
        using (Py.GIL())
            _robot.OnTick();
    }

    protected override void OnStop()
    {
        using (Py.GIL())
            _robot.OnStop();
    }
}