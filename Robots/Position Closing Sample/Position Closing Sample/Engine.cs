using System;
using System.Runtime.InteropServices;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Robots;

public partial class PositionClosingSample : Robot
{
    private RobotBridge _robot;
    private bool? _pythonIsSupported;
    private const string MainPythonFile = "Position Closing Sample_main.py";

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
            var className = nameof(PositionClosingSample);

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

    protected override void OnTimer()
    {
        if (!CanExecutePythonAlgorithm())
            return;

        using (Py.GIL())
            _robot.OnTimer();
    }

    protected override void OnException(Exception exception)
    {
        if (!CanExecutePythonAlgorithm())
            return;

        using (Py.GIL())
            _robot.OnException(exception);
    }

    protected override double GetFitness(GetFitnessArgs args)
    {
        using (Py.GIL())
            return _robot.GetFitness(args);
    }

    private bool CanExecutePythonAlgorithm()
    {
        if (_pythonIsSupported == false)
            return false;

        if (_pythonIsSupported == true)
            return true;

        if (!IsPlatformSupported())
        {
            Print("Python algorithms are not supported in the current version of cTrader");
            _pythonIsSupported = false;
            return false;
        }

        _pythonIsSupported = true;
        return true;
    }

    private bool IsPlatformSupported()
    {
        var version = Application.Version;

        if (RuntimeInformation.IsOSPlatform(OSPlatform.Windows) &&
            (version.Major > 5 || version.Major == 5 && version.Minor >= 4))
            return true;

        if (RuntimeInformation.IsOSPlatform(OSPlatform.OSX) &&
            (version.Major > 5 || version.Major == 5 && version.Minor >= 7))
            return true;

        if (RuntimeInformation.IsOSPlatform(OSPlatform.Linux) || RuntimeInformation.IsOSPlatform(OSPlatform.FreeBSD))
            return true;

        return false;
    }
}