using System;
using System.Linq;
using Python.Runtime;

namespace cAlgo.Robots;

internal class SafeExecuteMethodProxy
{
    readonly Func<object[], PyObject> _invokeAction;

    public bool HasMethod { get; private set; }
    
    public SafeExecuteMethodProxy(PyObject objectInstance, string methodName)
    {
        if (objectInstance.HasAttr(methodName))
        {
            HasMethod = true;
            var methodAttribute = objectInstance.GetAttr(methodName);
            _invokeAction = args => methodAttribute.Invoke(args.Select(arg => arg.ToPython()).ToArray());
        }
        else _invokeAction = _ => null;
    }

    public PyObject Invoke(params object[] args)
    {
        return _invokeAction(args);
    }
}