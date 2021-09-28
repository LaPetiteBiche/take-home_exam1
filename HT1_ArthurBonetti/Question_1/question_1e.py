from second_diff import *

f1 = sym.exp(x_var)
f2 = sym.cos(x_var)
f3 = sym.ln(x_var)

a, b = second_diff(f1,0)
print (f'The Estimated second derivative of {f1} at x = 0 is {a}, the error from the true value is {b}')
a, b = second_diff(f2,2*math.pi)
print (f'The Estimated second derivative of {f2} at x = {2*math.pi} is {a}, the error from the true value is {b}')
a, b = second_diff(f3,1)
print (f'The Estimated second derivative of {f3} at x = 1 is {a}, the error from the true value is {b}')
