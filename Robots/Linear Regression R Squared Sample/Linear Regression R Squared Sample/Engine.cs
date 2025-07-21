using System;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Robots;

public partial class LinearRegressionRSquaredSample
{
    private RobotBridge _robot;
    private const string MainPythonFile = "Linear Regression R Squared Sample_main.py";
    
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
                    _robot = new RobotBridge(pythonClass());

                    Positions.Closed += OnPositionClosed;
                    Positions.Opened += OnPositionOpened;

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

        Positions.Closed -= OnPositionClosed;
        Positions.Opened -= OnPositionOpened;
    }

    protected override void OnBar()
    {
        using (Py.GIL())
            _robot.OnBar();
    }

    protected override void OnBarClosed()
    {
        using (Py.GIL())
            _robot.OnBarClosed();
    }

    private void OnPositionClosed(PositionClosedEventArgs args)
    {
        using (Py.GIL())
            _robot.OnPositionClosed(args.Position);
    }

    private void OnPositionOpened(PositionOpenedEventArgs args)
    {
        using (Py.GIL())
            _robot.OnPositionOpened(args.Position);
    }
}