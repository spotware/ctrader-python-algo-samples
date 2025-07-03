namespace cAlgo.Plugins;
using Python.Runtime;

internal class PluginBridge
{
    private readonly SafeExecuteMethodProxy _onStartProxy;
    private readonly SafeExecuteMethodProxy _onStopProxy;

    internal PluginBridge(PyObject objectInstance)
    {
        _onStartProxy = new SafeExecuteMethodProxy(objectInstance, "on_start");
        _onStopProxy = new SafeExecuteMethodProxy(objectInstance, "on_stop");
    }

    internal void OnStart()
    {
        _onStartProxy.Invoke();
    }

    internal void OnStop()
    {
        _onStopProxy.Invoke();
    }
}