using System;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.FullAccess)]
public class AccessRightSample : Indicator
{
    private IndicatorBridge _indicator;
    private const string MainPythonFile = "Access Right Sample_main.py";

    protected override void Initialize()
    {
        EngineHelper.Initialize(this);

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
                    _indicator = new IndicatorBridge(pythonClass());

                    _indicator.Initialize();
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
    }
}