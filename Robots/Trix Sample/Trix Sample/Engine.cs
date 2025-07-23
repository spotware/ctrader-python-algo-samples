using System;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Robots;

public partial class TrixSample
{
    private RobotBridge _robot;
    private const string MainPythonFile = "Trix Sample_main.py";
    
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

    [Obsolete("Subscribe to Positions.Closed event instead")]
    protected override void OnPositionClosed(Position position)
    {
        using (Py.GIL())
            _robot.OnPositionClosed(position);
    }

    [Obsolete("Subscribe to Positions.Closed event instead")]
    protected override void OnPositionOpened(Position openedPosition)
    {
        using (Py.GIL())
            _robot.OnPositionOpened(openedPosition);
    }
}