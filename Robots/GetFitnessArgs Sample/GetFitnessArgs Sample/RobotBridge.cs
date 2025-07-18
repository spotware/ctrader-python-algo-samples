using System.Globalization;
using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Robots;

internal class RobotBridge : BaseBridge
{
    private readonly SafeExecuteMethodProxy _onStartProxy;
    private readonly SafeExecuteMethodProxy _onTickProxy;
    private readonly SafeExecuteMethodProxy _onStopProxy;
    private readonly SafeExecuteMethodProxy _onBarProxy;
    private readonly SafeExecuteMethodProxy _onBarClosedProxy;
    private readonly SafeExecuteMethodWithResultProxy<double> _getFitnessProxy;
    private readonly SafeExecuteMethodProxy _onPositionClosedProxy;
    private readonly SafeExecuteMethodProxy _onPositionOpenedProxy;

    internal RobotBridge(PyObject objectInstance)
        : base(objectInstance)
    {
        var numberFormatInfo = new NumberFormatInfo();

        _onStartProxy = new SafeExecuteMethodProxy(objectInstance, "on_start");
        _onTickProxy = new SafeExecuteMethodProxy(objectInstance, "on_tick");
        _onStopProxy = new SafeExecuteMethodProxy(objectInstance, "on_stop");
        _onBarProxy = new SafeExecuteMethodProxy(objectInstance, "on_bar");
        _getFitnessProxy = new SafeExecuteMethodWithResultProxy<double>(objectInstance, "get_fitness", pr => pr.ToDouble(numberFormatInfo), _ => 0);
        _onBarClosedProxy = new SafeExecuteMethodProxy(objectInstance, "on_bar_closed");
        _onPositionClosedProxy = new SafeExecuteMethodProxy(objectInstance, "on_position_closed");
        _onPositionOpenedProxy = new SafeExecuteMethodProxy(objectInstance, "on_position_opened");
    }

    internal void OnStart()
    {
        _onStartProxy.Invoke();
    }

    internal void OnTick()
    {
        _onTickProxy.Invoke();
    }

    internal void OnStop()
    {
        _onStopProxy.Invoke();
    }

    internal void OnBar()
    {
        _onBarProxy.Invoke();
    }

    internal void OnBarClosed()
    {
        _onBarClosedProxy.Invoke();
    }

    internal void OnPositionClosed(Position position)
    {
        _onPositionClosedProxy.Invoke(position);
    }

    internal void OnPositionOpened(Position openedPosition)
    {
        _onPositionOpenedProxy.Invoke(openedPosition);
    }
    
    internal double GetFitness(GetFitnessArgs args)
    {
        return _getFitnessProxy.Invoke(args);
    }
}