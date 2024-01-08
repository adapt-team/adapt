
import js2py

def executeJS(filename):
    with open(filename) as code:
        res = code.read()
        
    context = js2py.EvalJs()
    result = context.execute(res)

    print(context.result)