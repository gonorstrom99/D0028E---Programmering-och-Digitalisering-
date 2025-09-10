import math
def derivative(f,x,h):
    return((f(x+h)-f(x-h))/(2*h))

def f1(x):
    return 2*x
def f2(x):
    return x**2-1
def f3(x):
    return 2**x-1
def f4(x):
    return (x-math.e**(-x))
# print(derivative(math.sin,0,0.00000000000001))
# print(derivative(f1,3,0.00000000000001))
# print(derivative(f2,3,0.1))


def solve(f,x0,h):
    xn=x0
    xn1=xn-f(xn)/derivative(f,xn,h)
    
    while(abs(xn1-xn)>h):
        
        xn=xn1
        xn1=xn1-f(xn1)/derivative(f,xn1,h)
    return xn1

print(solve(f4,-20,0.00000001))

import d0028e_lab2_solveTest

