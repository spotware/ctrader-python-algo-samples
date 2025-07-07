using System;
using System.Linq;
using Python.Runtime;

namespace cAlgo.Robots;

internal class SafeExecuteMethodProxy
{
    readonly Action<object[]> _invokeAction;

    public SafeExecuteMethodProxy(PyObject objectInstance, string methodName)
    {
        if (objectInstance.HasAttr(methodName))
        {
            var methodAttribute = objectInstance.GetAttr(methodName);
            _invokeAction = args => methodAttribute.Invoke(args.Select(arg => arg.ToPython()).ToArray());
        }
        else _invokeAction = _ => { };
    }

    public void Invoke(params object[] args)
    {
        _invokeAction(args);
    }
}