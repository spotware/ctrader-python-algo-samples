using System;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None)]
public class TestIndicator : Indicator
{
    private dynamic _indicator;
    private IntPtr _pythonThreadState;
    private const string MainPythonFile = $"{nameof(TestIndicator)}.{nameof(TestIndicator)}.py";


    [Output("Main")]
    public IndicatorDataSeries Result { get; set; }

    protected override void Initialize()
    {
        var pythonDllPath = Environment.GetEnvironmentVariable("__CT_ALGOHOST_ENDPOINT_PYTHON_DLL_PATH");
        if (string.IsNullOrEmpty(pythonDllPath))
            throw new InvalidOperationException("Python runtime not found! Please recompile and restart indicator");

        if (!PythonEngine.IsInitialized)
        {
            Runtime.PythonDLL = pythonDllPath;
            PythonEngine.Initialize();
        }

        _pythonThreadState = PythonEngine.BeginAllowThreads();

        using (Py.GIL())
        {
            var pythonFolder = EngineHelper.CreatePythonFolder();
            EngineHelper.CopyPythonResources(pythonFolder, MainPythonFile, nameof(TestIndicator));

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
                    _indicator = pythonClass();

                    _indicator.OnStart();
                }
                catch (Exception ex)
                {
                    Print($"Error initializing Python: {ex.Message}\nStack trace: {ex.StackTrace}");
                    throw;
                }
            }
        }
    }

    public override void Calculate(int index)
    {
        using (Py.GIL())
            _indicator.Calculate(index);
    }

    protected override void OnDestroy()
    {
        using (Py.GIL())
            _indicator.OnDestroy();

        PythonEngine.EndAllowThreads(_pythonThreadState);

        if (PythonEngine.IsInitialized)
            PythonEngine.Shutdown();
    }
}