using System;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Robots;

public partial class PositionEventsSample : Robot
{
    private RobotBridge _robot;
    private const string MainPythonFile = "Position Events Sample_main.py";

    protected override void OnStart()
    {
        EngineHelper.Initialize(this, Print);

        using (Py.GIL())
        {
            var code = EmbeddedResourceProvider.ReadText(MainPythonFile);
            var className = nameof(PositionEventsSample);

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

    protected override void OnTimer()
    {
        using (Py.GIL())
            _robot.OnTimer();
    }

    protected override void OnException(Exception exception)
    {
        using (Py.GIL())
            _robot.OnException(exception);
    }

    protected override double GetFitness(GetFitnessArgs args)
    {
        using (Py.GIL())
            return _robot.GetFitness(args);
    }
}