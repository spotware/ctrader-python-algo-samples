using cAlgo.API;
using Python.Runtime;

namespace cAlgo.Robots;

internal class RobotBridge
{
    private readonly SafeExecuteMethodProxy _onStartProxy;
    private readonly SafeExecuteMethodProxy _onTickProxy;
    private readonly SafeExecuteMethodProxy _onStopProxy;
    private readonly SafeExecuteMethodProxy _onBarProxy;
    private readonly SafeExecuteMethodProxy _onPositionClosedProxy;
    private readonly SafeExecuteMethodProxy _onPositionOpenedProxy;

    internal RobotBridge(PyObject objectInstance)
    {
        _onStartProxy = new SafeExecuteMethodProxy(objectInstance, "on_start");
        _onTickProxy = new SafeExecuteMethodProxy(objectInstance, "on_tick");
        _onStopProxy = new SafeExecuteMethodProxy(objectInstance, "on_stop");
        _onBarProxy = new SafeExecuteMethodProxy(objectInstance, "on_bar");
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

    internal void OnPositionClosed(Position position)
    {
        _onPositionClosedProxy.Invoke(position);
    }

    internal void OnPositionOpened(Position openedPosition)
    {
        _onPositionOpenedProxy.Invoke(openedPosition);
    }
}