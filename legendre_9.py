
#legendre polynomial
#(9) integrate(-1 --> 1)(P(n,x)*P(m,x)) = (2*dmn)/(2*n+1)

import numpy as np
from scipy.special import legendre
from scipy.misc import derivative
from scipy.integrate import quad

def f(x):
    return (legendre(m)(x))*(legendre(n)(x)) 

x=float(input("Enter the x: "))
m=int(input("Enter the m: "))
n=int(input("Enter the n: "))
LHS=quad(f,-1,1)[0]

if(m==n):
    d=1
    RHS=((2.0*d)/(2*n+1))
    print("(m==n):\n",RHS)
elif(m!=n):
    d=0
    RHS=((2.0*d)/(2*n+1))
    print("(m!=n): ",RHS)
print("LHS:\n",LHS)
