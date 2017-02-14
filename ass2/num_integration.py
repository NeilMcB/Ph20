import math
import numpy as np
import matplotlib.pyplot as plt

#Q2

#Applies the extended trapezoidal rule
#to func to numerically integrate from
#a to b using N steps. Returns the 
#numerical answer.
def extended_trapezoid(func, a, b, N):
    #prevent integer division
    a = float(a)
    b = float(b)
    
    #determine bin width
    hN = (b-a)/N
    
    #create array of x values
    xs = np.linspace(a, b, N+1)
    
    #apply function to each value in xs
    func = np.vectorize(func)
    fs = func(xs)
    
    #adjust for double counting of first and last fs
    fs[0]  /= 2
    fs[-1] /= 2
    
    #sum over all fs
    f = hN*np.sum(fs)
    
    return f

#Q3

#Applies the extended Simpson's rule
#to func to numerically integrate from
#a to b using N steps. Returns the 
#numerical answer.
def extended_simpson(func, a, b, N):
    #prevent integer division
    a = float(a)
    b = float(b)
    
    #determine bin width
    hN = (b-a)/N
    
    #create array of x values
    #including a point c for every cut
    xs = np.linspace(a, b, 2*N+1)
    
    #apply function to each value in xs
    func = np.vectorize(func)
    fs = func(xs)/6.
    
    #adjust every even (a,b) inner element
    fs[2:2*N:2] *= 2
    #adjust every odd (c) element
    fs[1::2] *= 4
     
    #sum over all fs
    f = hN*np.sum(fs)
    
    return f

#Q4

#Produces a plot to compare the 
#accuracy of simpson and trapezoidal
#methods for various N
def error_convergence(func, a, b, Ns=np.logspace(1,4, num=10)):
    #from PSheet
    e_true = 1.7182818284590452354
    #assure np array used
    Ns = np.array(Ns).astype('int')
        
    trapezoid_errs = np.array([abs(extended_trapezoid(func, a, b , N) - e_true) for N in Ns])
    simpson_errs   = np.array([abs(extended_simpson(func, a, b , N) - e_true) for N in Ns])

    trapezoid_conv = np.absolute(np.ediff1d(trapezoid_errs))
    simpson_conv   = np.absolute(np.ediff1d(simpson_errs))
    
    #initialise plot for graphing
    fig, ax = plt.subplots(nrows=1, ncols=1)
    #plot both methods
    ax.loglog(Ns[1:], trapezoid_conv, label="Trapezoidal")
    ax.loglog(Ns[1:], simpson_conv, label="Simpson")
    #make plot pretty :)
    ax.set_xlim([0, Ns.max()])
    ax.set_xlabel("N steps")
    ax.set_ylabel("Convergence")
    ax.set_title("Convergence of Numerical Integration Methods")
    ax.legend()
    #save and close plot
    fig.savefig("err_convergence.pdf")
    plt.close(fig)

#Q5

#Applies the extended Simpson's rule
#to func to numerically integrate from
#a to b until a relative accuracy
#of acc is achieved. Returns the 
#numerical answer and the number of 
#splits required.
def extended_simpson_acc(func, a, b, acc):
    err = acc + 1. #ensure first loop occurs
    N0 = 1         #number of steps to try first
    k  = 1         #exponentiating factor
    int_prev = 0   #to store previous loop value
    
    #repeat calculations until desired accuracy achieved
    while(err > acc):
        N = (2**k)*N0
        int_curr = extended_simpson(func, a, b, (2**k)*N0)
        err = abs((int_curr-int_prev)/int_curr)
        
        #update stored value for comparison
        int_prev = int_curr
        k += 1
        
    return (int_curr, N)