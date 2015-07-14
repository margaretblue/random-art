import random
import math

# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.


def create_expression():
    cos = math.cos
    sin = math.sin
    tan = math.tan
    pi = math.pi

    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""
    # expr = lambda x, y: (random.random() * (cos(x) ** 2) * x + (sin(x) **2) * x )
    # expr = lambda x, y: (random.uniform(cos(x), sin(y) * sin(sin(pi * sin(pi * (sin(pi * sin(pi * sin(pi * cos(pi * y)))))

    # expr = lambda x, y: (random.random() * 2) - 1
    #expr = lambda x, y: (random.random() * cos(x)) - 1
    expr = lambda x, y: (random.uniform(cos(x), sin(y) * sin(sin(pi * sin(pi * (sin(pi * sin(pi * sin(pi * cos(pi * y))))) * cos(pi * sin(pi * cos(pi * (pi * y) * (x * x)))))))))


    return expr

def picker():
    cos = math.cos
    sin = math.sin
    tan = math.tan
    pi = math.pi
    expressions = [
        lambda x, y: (random.uniform(cos(x), sin(y) * sin(sin(pi * sin(pi * (sin(pi * sin(pi * sin(pi * cos(pi * y))))) * cos(pi * sin(pi * cos(pi * (pi * y) * (x * x)))))))))
    ]
    return expressions



def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr(x, y)
