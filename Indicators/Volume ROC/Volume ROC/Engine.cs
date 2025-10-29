using cAlgo.API;
using Python.Runtime;
using System;
using System.Runtime.InteropServices;

namespace cAlgo.Indicators;

public partial class VolumeROC : Indicator
{
    private IndicatorBridge _indicator;
    private const string MainPythonFile = "Volume ROC_main.py";
    private bool? _pythonIsSupported;

    protected override void Initialize()
    {
        if (!CanExecutePythonAlgorithm())
            return;

        EngineHelper.Initialize(this, Print);

        using (Py.GIL())
        {
            var code = EmbeddedResourceProvider.ReadText(MainPythonFile);
            var className = nameof(VolumeROC);;

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
        if (!CanExecutePythonAlgorithm())
            return;

        using (Py.GIL())
            _indicator.Calculate(index);
    }

    protected override void OnDestroy()
    {
        if (!CanExecutePythonAlgorithm())
            return;

        using (Py.GIL())
            _indicator.OnDestroy();
    }

    protected override void OnTimer()
    {
        if (!CanExecutePythonAlgorithm())
            return;

        using (Py.GIL())
            _indicator.OnTimer();
    }

    protected override void OnException(Exception exception)
    {
        if (!CanExecutePythonAlgorithm())
        {
            base.OnException(exception);
            return;
        }

        using (Py.GIL())
            _indicator.OnException(exception);
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
            (version.Major > 5 || (version.Major == 5 && version.Minor >= 4)))
            return true;

        if (RuntimeInformation.IsOSPlatform(OSPlatform.OSX) &&
            (version.Major > 5 || (version.Major == 5 && version.Minor >= 7)))
            return true;

        if (RuntimeInformation.IsOSPlatform(OSPlatform.Linux) || RuntimeInformation.IsOSPlatform(OSPlatform.FreeBSD))
            return true;

        return false;
    }
}