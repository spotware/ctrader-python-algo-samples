using System;
using System.Runtime.InteropServices;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Robots;

public partial class ChartIndicatorsSample 
{
    private RobotBridge _robot;
    private bool? _pythonIsSupported;
    private const string MainPythonFile = "ChartIndicators Sample_main.py";
    
    protected override void OnStart()
    {
        if (!CanExecutePythonAlgorithm())
        {
            Stop();
            return;
        }

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
        if (!CanExecutePythonAlgorithm())
            return;

        using (Py.GIL())
            _robot.OnTick();
    }

    protected override void OnStop()
    {
        if (!CanExecutePythonAlgorithm())
            return;

        using (Py.GIL())
            _robot.OnStop();

        Positions.Closed -= OnPositionClosed;
        Positions.Opened -= OnPositionOpened;
    }

    protected override void OnBar()
    {
        if (!CanExecutePythonAlgorithm())
            return;

        using (Py.GIL())
            _robot.OnBar();
    }

    protected override void OnBarClosed()
    {
        if (!CanExecutePythonAlgorithm())
            return;

        using (Py.GIL())
            _robot.OnBarClosed();
    }

    private void OnPositionClosed(PositionClosedEventArgs args)
    {
        if (!CanExecutePythonAlgorithm())
            return;

        using (Py.GIL())
            _robot.OnPositionClosed(args.Position);
    }

    private void OnPositionOpened(PositionOpenedEventArgs args)
    {
        if (!CanExecutePythonAlgorithm())
            return;

        using (Py.GIL())
            _robot.OnPositionOpened(args.Position);
    }

    private bool CanExecutePythonAlgorithm
    {
        if _pythonIsSupported == false
            return false;

        if _pythonIsSupported == true
            return true;

        if !IsPlatformSupported
        {
            Print"Python algorithms are not supported in the current version of cTrader";
            _pythonIsSupported = false;
            return false;
        }

        _pythonIsSupported = true;
        return true;
    }

    private bool IsPlatformSupported
    {
        var version = Application.Version;

        if RuntimeInformation.IsOSPlatformOSPlatform.Windows &&
            version.Major > 5 || version.Major == 5 && version.Minor >= 4
            return true;

        if RuntimeInformation.IsOSPlatformOSPlatform.OSX &&
            version.Major > 5 || version.Major == 5 && version.Minor >= 7
            return true;

        return false;
    }
}