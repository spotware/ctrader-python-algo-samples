using System.Linq;
using Python.Runtime;

namespace cAlgo.Robots;

internal class SafeExecuteMethodProxy
{
    private readonly PyObject _objectInstance;
    private readonly string _methodName;
    private PyObject _methodAttribute;

    public SafeExecuteMethodProxy(PyObject objectInstance, string methodName)
    {
        _objectInstance = objectInstance;
        _methodName = methodName;
    }

    public void Invoke(params object[] args)
    {
        _methodAttribute ??= _objectInstance.GetAttr(_methodName);
        _methodAttribute?.Invoke(args.Select(arg => arg.ToPython()).ToArray());
    }
}