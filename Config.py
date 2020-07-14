import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')

def f(thetas, t, eta, kappa, I):

    return 1-np.cos(thetas) + (1+np.cos(thetas))*(eta+kappa*I)

def I_fun(an, thetas, n):
    S = 0
    #print("Thetas = ", thetas)
    for i in range(len(thetas)):
        s = (1-np.cos(thetas[i]))**n
        #print("s = ", s)
        S += s
        
    I = an/len(thetas) * S
    return I

def an_fun(n):
    return 2**n*(factorial(n))**2/factorial(2*n)

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact*i
    return(fact)

def euler(f, eta, kappa, y0=1, h=1e-3, N=100):
    y = np.ones((len(y0), N))
    y[:, 0] = y0
    #print("y first =", y)
    t = 0
    n = 2
    for i in range(N-1):
        an = an_fun(n=n)
        #print("an = ", an)
        I = I_fun(an, y[:, i], n=n)
        #print("I = ", I)
        y[:, i+1] = y[:, i] + h*f(thetas=y[:, i], t=t, eta=eta, kappa=kappa, I=I)
        #print("y = ", y)
        t += h
    return(y)

        
        
    