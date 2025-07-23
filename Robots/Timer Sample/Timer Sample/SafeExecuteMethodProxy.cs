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

internal class SafeExecuteMethodWithResultProxy<T>
{
    readonly Func<object[], T> _invokeFunc;

    public SafeExecuteMethodWithResultProxy(
        PyObject objectInstance,
        string methodName,
        Func<PyObject, T> converter,
        Func<object[], T> fullbackFunc)
    {
        if (objectInstance.HasAttr(methodName))
        {
            var methodAttribute = objectInstance.GetAttr(methodName);
            _invokeFunc = args =>
            {
                var pyResult = methodAttribute.Invoke(args.Select(arg => arg.ToPython()).ToArray());
                return converter(pyResult);
            };
        }
        else _invokeFunc = fullbackFunc;
    }

    public T Invoke(params object[] args)
    {
        return _invokeFunc(args);
    }
}