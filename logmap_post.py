#!/usr/bin/env python

"""
Code for Population Dynamics (W.Kinzel/G.Reents, Physics by Computer)

This code is based on logmap.m listed in Appendix E of the book and will
replicate Figs. 3.1-3.7 of the book.
"""

__author__ = "Christian Alis"
__credits__ = "W.Kinzel/G.Reents"

import numpy as np
import matplotlib.pyplot as plt

f = lambda x, r: 4 * r * x * (1-x)

def iterf(f, x0, r, n):
    # Add a docstring for this function. Parameters should be properly
    # documented and the docstring itself should follow the scipy/numpy
    # docstring convention and ReST format
    
    # Is it possible to vectorize this function? Explain why or why not.
    out = [x0]
    for _ in xrange(n):
        out.append(f(out[-1], r))
    return out

def plot_3_1(f=f, x0=0.65, r=0.87, maxiter=40):
    # Add a docstring for this function. Parameters should be properly
    # documented and the docstring itself should follow the scipy/numpy
    # docstring convention and ReST format
    ns = range(maxiter+1)
    xs = iterf(f, x0, r, maxiter)
    plt.plot(ns, xs, '--o')
    plt.xlim(0, maxiter+1)
    # add axis labels
    plt.show()
    
def plot_3_2(f=f, r=0.87):
    # Add a docstring for this function. Parameters should be properly
    # documented and the docstring itself should follow the scipy/numpy
    # docstring convention and ReST format
    x = np.linspace(0, 1, 500)
    fx1 = f(x, r)
    fx2 = f(fx1, r)
    # complete the following two lines
    fx3 = # ...
    fx4 = # ...
    plt.plot(x, x, 'k')
    plt.plot(x, fx1, '--', color='gray')
    # What is the python type of the value of color?
    # What would happen if (0.6)*3 is used instead of (0.6,)*3?
    # What would happen if (0.3,)*3 is used instead of (0.6,)*3?
    # What would happen if (0.9,)*3 is used instead of (0.6,)*3?
    plt.plot(x, fx2, color=(0.6,)*3)
    plt.plot(x, fx4, 'k')
    # add axis labels
    plt.show()
    
def plot_3_3(x0=0.3, r_min=0, r_max=1):
    # Add a docstring for this function. Parameters should be properly
    # documented and the docstring itself should follow the scipy/numpy
    # docstring convention and ReST format
    rs = np.linspace(r_min, r_max, 500)
    # What is the purpose of multiplying the output of np.ones() and a number?
    # What are the dimensions of fxs?
    # What do the rows and columns of fxs represent?
    fxs = np.array(iterf(f, np.ones(len(rs))*0.3, rs, 1000))
    # What are the dimensions of fxs?
    # What does .T in the second argument do?
    # Can we use fxs[100:,:] instead of fxs[100:,:].T? Why or why not?
    # What does the keyword ms do?
    plt.plot(rs, fxs[100:,:].T, 'k.', ms=2)
    # add axis labels
    plt.show()
    
def plot_3_4(x0=0.3):
    # Add a docstring for this function. Parameters should be properly
    # documented and the docstring itself should follow the scipy/numpy
    # docstring convention and ReST format
    plot_3_3(r_min=0.88)
    
def plot_3_5(x0=0.3, r = 0.934):
    # Add a docstring for this function. Parameters should be properly
    # documented and the docstring itself should follow the scipy/numpy
    # docstring convention and ReST format
    
    # Complete the following line
    fxs = iterf(# ...
    plt.hist(fxs, bins=100)
    plt.xlim(xmin=0)
    # add axis labels
    plt.show()
    
def plot_3_6(x0=0.3, r=0.874640, maxiter=1000):
    # Add a docstring for this function. Parameters should be properly
    # documented and the docstring itself should follow the scipy/numpy
    # docstring convention and ReST format
    xs = np.linspace(0, 1)
    fxs = iterf(f, x0, r, 1000)[100:]
    # complete the next two lines
    plt.plot(xs, #...
    plt.plot(xs, #...
    # What are the first 10 elements of the first argument of the ff. 
    # plt.plot() call?
    # Why was the last element of fxs omitted in the argument of np.repeat()?
    # Can we use fxs[:-1]*2 instead of np.repeat(fxs[:-1], 2)? Why or why not?
    plt.plot(np.repeat(fxs[:-1], 2), 
    # What does the following argument of plt.plot() call represent?
    # What are the dimensions/shape of the following plt.plot() argument?
    # What are the dimensions of the argument of np.column_stack()?
    # Why was the first element of fxs[1:] omitted?
    # What would happen if .ravel() is removed?
    # Can we use np.ravel(zip(fxs[:,1], fxs[1:])) instead of 
    # np.column_stack((fxs[:-1], fxs[1:])).ravel()? Why or why not?
             np.column_stack((fxs[:-1], fxs[1:])).ravel(), 
             '-o')
    # add axis labels
    plt.show()
    
def plot_3_7(x0=0.3, r=0.96420, maxiter=1000):
    # Add a docstring for this function. Parameters should be properly
    # documented and the docstring itself should follow the scipy/numpy
    # docstring convention and ReST format
    
    # complete the following line
    plot_3_6(# ...
    
# OPTIONAL:
# * Replace np.ones(len(rs))*0.3 with an equivalent expression that uses
#   the Python standard library only (no numpy)
# * write iterf() as a recursive function
# * estimate the Feigenbaum constant
# * add interactivity to your plots

if __name__ == "__main__":
    plot_3_1()
    plot_3_2()
    plot_3_3()
    plot_3_4()
    plot_3_5()
    plot_3_6()
    plot_3_7()