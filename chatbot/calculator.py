def calculate(expression):
    try:
        return eval(expression)
    except:
        return "Invalid Expression"