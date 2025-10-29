using Python.Runtime;

namespace cAlgo.Indicators;

internal class IndicatorBridge : BaseBridge
{
    private readonly SafeExecuteMethodProxy _initializeProxy;
    private readonly SafeExecuteMethodProxy _calculateProxy;
    private readonly SafeExecuteMethodProxy _onDestroyProxy;

    internal IndicatorBridge(PyObject objectInstance)
        : base(objectInstance)
    {
        _initializeProxy = new SafeExecuteMethodProxy(objectInstance, "initialize");
        _calculateProxy = new SafeExecuteMethodProxy(objectInstance, "calculate");
        _onDestroyProxy = new SafeExecuteMethodProxy(objectInstance, "on_destroy");
    }

    internal void Initialize()
    {
        _initializeProxy.Invoke();
    }

    internal void Calculate(int index)
    {
        _calculateProxy.Invoke(index);
    }

    internal void OnDestroy()
    {
        _onDestroyProxy.Invoke();
    }
}