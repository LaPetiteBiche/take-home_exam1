import math
def poisson(k, lam):
    top = (lam**k)*math.exp(-lam)
    bot = math.factorial(k)
    return (top/bot)