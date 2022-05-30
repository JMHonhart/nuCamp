"""
Example of operations
By Jack
Date
"""


def do_add(x, y):
    """
    Adds two inputs

    Arguments:
    x
    y

    Return result or None
    """
    res = ""
    try:
        res = x + y
    except TypeError:
        print(str(x) + " can not be added to " + str(y))
        return None
    else:
        print(str(x) + " + " + str(y) + " = " + str(res))

    return res


do_add(1, 2)


def do_sub(x, y):
    """
    Subtract two inputs

    Arguments:
    x
    y

    Return result or None
    """
    res = ""
    try:
        res = x - y
    except TypeError:
        print(str(y) + " can not be subtracted from " + str(x))
        return None
    else:
        print(str(x) + " - " + str(y) + " = " + str(res))

    return res


def do_mult(x, y):
    """
    Multiply two inputs

    Arguments:
    x
    y

    Return result or None
    """
    res = ""
    try:
        res = x * y
    except TypeError:
        print(str(x) + " can not be multiplied by " + str(y))
        return None
    else:
        print(str(x) + " * " + str(y) + " = " + str(res))

    return res


def do_div(x, y):
    """
    Divide two inputs

    Arguments:
    x
    y

    Return result or None
    """
    res = ""
    try:
        res = x / y
    except TypeError:
        print(str(x) + " can not be divided by " + str(y))
        return None
    else:
        print(str(x) + " / " + str(y) + " = " + str(res))

    return res


def do_div_whole(x, y):
    """
    Whole division two inputs

    Arguments:
    x
    y

    Return result or None
    """
    res = ""
    try:
        res = x // y
    except TypeError:
        print(str(x) + " can not be divided by " + str(y))
        return None
    else:
        print(str(x) + " // " + str(y) + " = " + str(res))

    return res


def do_mod(x, y):
    """
    Modulus two inputs

    Arguments:
    x
    y

    Return result or None
    """
    res = ""
    try:
        res = x % y
    except TypeError:
        print(str(x) + " can not modulo by " + str(y))
        return None
    else:
        print(str(x) + " % " + str(y) + " = " + str(res))

    return res


def do_exp(x, y):
    """
    Adds two inputs

    Arguments:
    x
    y

    Return result or None
    """
    res = ""
    try:
        res = x ** y
    except TypeError:
        print(str(x) + " can not exponent by " + str(y))
        return None
    else:
        print(str(x) + " ** " + str(y) + " = " + str(res))

    return res


print("--- Addition ---")
do_add(1, 1)
do_add(1, -1)
do_add(1, 1.0)
do_add(1.0, -1)
do_add(-1, 1.0)
do_add(1, "fobar")

print("--- Subtraction ---")
do_sub(1, 1)
do_sub(1, -1)
do_sub(1, 1.0)
do_sub(1.0, -1)
do_sub(-1, 1.0)
do_sub(1, "fobar")

print("--- Multiplication ---")
do_mult(1, 1)
do_mult(1, -1)
do_mult(1, 1.0)
do_mult(1.0, -1)
do_mult(-1, 1.0)
do_mult(1, "fobar")

print("--- Division ---")
do_div(1, 1)
do_div(1, -1)
do_div(1, 1.0)
do_div(1.0, -1)
do_div(-1, 1.0)
do_div(1, "fobar")

print("--- Whole Division ---")
do_div_whole(2, 1)
do_div_whole(2, -1)
do_div_whole(2, 3.0)
do_div_whole(3.0, -2)
do_div_whole(-2, 3.0)
do_div_whole(1, "fobar")

print("--- Modulo (Remainder Division) ---")
do_mod(1, 1)
do_mod(1, -1)
do_mod(1, 1.0)
do_mod(1.0, -1)
do_mod(-1, 1.0)
do_mod(1, "fobar")

print("--- Exponential ---")
do_exp(1, 1)
do_exp(1, -1)
do_exp(1, 1.0)
do_exp(1.0, -1)
do_exp(-1, 1.0)
do_exp(1, "fobar")
