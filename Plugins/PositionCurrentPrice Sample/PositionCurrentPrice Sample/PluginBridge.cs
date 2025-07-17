using Python.Runtime;

namespace cAlgo.Plugins;

internal class PluginBridge
{
    private readonly SafeExecuteMethodProxy _onStartProxy;
    private readonly SafeExecuteMethodProxy _onStopProxy;
    private readonly SafeExecuteMethodProxy _onTimerProxy;

    internal PluginBridge(PyObject objectInstance)
    {
        _onStartProxy = new SafeExecuteMethodProxy(objectInstance, "on_start");
        _onStopProxy = new SafeExecuteMethodProxy(objectInstance, "on_stop");
        _onTimerProxy = new SafeExecuteMethodProxy(objectInstance, "on_timer");
    }

    internal void OnStart()
    {
        _onStartProxy.Invoke();
    }

    internal void OnStop()
    {
        _onStopProxy.Invoke();
    }
    
    internal void OnTimer()
    {
        _onTimerProxy.Invoke();
    }
}