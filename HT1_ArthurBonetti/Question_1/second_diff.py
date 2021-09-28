import math
import sympy as sym
from sympy import symbols

x_var = symbols('x')


def second_diff(f,x,h=0.001):
    '''Approximate the second derivative of an arbitrary mathematical function with h=0.001, f is a scypy function and x is the point around which to approximate'''
    
    first = f.subs(x_var, x+h)
    second = f.subs(x_var, x)
    third = f.subs(x_var, x-h)
    deriv = (first - 2*second + third)/h**2
    true_deriv = sym.diff(f, x_var, 2)
    true_deriv = true_deriv.subs(x_var, x)
    error = abs(deriv - true_deriv)
    return (deriv, error)

