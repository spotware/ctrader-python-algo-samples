using System;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Indicators;

[Indicator(AccessRights = AccessRights.None, IsOverlay = true)]
[Cloud("Top", "Bottom", Opacity = 0.2)]
public class BollingerBandsCloudSample : Indicator
{
    private IndicatorBridge _indicator;
    private const string MainPythonFile = "Bollinger Bands Cloud Sample_main.py";
    
    [Output("Main", LineColor = "Yellow", PlotType = PlotType.Line, Thickness = 1)]
    public IndicatorDataSeries Main { get; set; }

    [Output("Top", LineColor = "Red", PlotType = PlotType.Line, Thickness = 1)]
    public IndicatorDataSeries Top { get; set; }

    [Output("Bottom", LineColor = "Red", PlotType = PlotType.Line, Thickness = 1)]
    public IndicatorDataSeries Bottom { get; set; }

    protected override void Initialize()
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