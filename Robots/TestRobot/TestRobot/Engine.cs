using System;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Robots;

[Robot(AccessRights = AccessRights.None, AddIndicators = true)]
public class TestRobot : Robot
{
    private dynamic _robot;
    private IntPtr _pythonThreadState;
    private const string MainPythonFile = $"{nameof(TestRobot)}.{nameof(TestRobot)}.py";

    protected override void OnStart()
    {
        var pythonDllPath = Environment.GetEnvironmentVariable("__CT_ALGOHOST_ENDPOINT_PYTHON_DLL_PATH");
        if (string.IsNullOrEmpty(pythonDllPath))
            throw new InvalidOperationException("Python runtime not found! Please recompile and restart robot");

        if (!PythonEngine.IsInitialized)
        {
            Runtime.PythonDLL = pythonDllPath;
            PythonEngine.Initialize();
        }

        _pythonThreadState = PythonEngine.BeginAllowThreads();

        using (Py.GIL())
        {
            var pythonFolder = EngineHelper.CreatePythonFolder();
            EngineHelper.CopyPythonResources(pythonFolder, MainPythonFile, nameof(TestRobot));

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

        PythonEngine.EndAllowThreads(_pythonThreadState);

        if (PythonEngine.IsInitialized)
            PythonEngine.Shutdown();
    }
}