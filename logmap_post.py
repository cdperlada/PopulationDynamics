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
    '''
    Iterate a function.
    
    Parameters
    ----------
    f : function
	    Function for iteration.
    x0 : float
	    Initial value for iteration.
    r : float
	    Parameter constant in f.
    n : int
         Number of iterations.
    '''
    
    # Is it possible to vectorize this function? Explain why or why not.
    '''No since each element depends on the previous element except for the first element, initial value.'''
    
    out = [x0]
    for _ in xrange(n):
        out.append(f(out[-1], r))
    return out

def plot_3_1(f=f, x0=0.65, r=0.87, maxiter=40):
    # Add a docstring for this function. Parameters should be properly
    # documented and the docstring itself should follow the scipy/numpy
    # docstring convention and ReST format
    '''
    Plot the value of x after n iterations.
	
    Parameters
    ----------
    f : function
	    Function for iteration.
    x0 : float
	    Initial value for iteration.
    r : float
	    Parameter constant in f.
    maxiter : int
	    Maximum nuber of iteration.
    '''
    
    ns = range(maxiter+1)
    xs = iterf(f, x0, r, maxiter)
    plt.plot(ns, xs, '--o')
    plt.xlim(0, maxiter+1)
    # add axis labels 
    plt.xlabel('$n$')
    plt.xticks([0, 10, 20, 30, 40], [0, 10, 20, 30, 40])
    plt.ylabel('$x(n)$')
    plt.ylim((0.4,0.9))
    plt.show()
    
def plot_3_2(f=f, r=0.87):
    # Add a docstring for this function. Parameters should be properly
    # documented and the docstring itself should follow the scipy/numpy
    # docstring convention and ReST format
    '''
    Plot the x,f(x) and its two-fold and four-fold iterations.
    
    Parameters
    ----------
    f : function
        Function for iteration.
    r : float
        Parameter constant in f.
    '''
    
    x = np.linspace(0, 1, 500)
    fx1 = f(x, r)
    fx2 = f(fx1, r)
    # complete the following two lines
    fx3 = f(fx2, r)
    fx4 = f(fx3, r)
    plt.plot(x, x, 'k',label='$x$')
    plt.plot(x, fx1, '--', color='gray', label='$f(x)$')
    # What is the python type of the value of color?
    '''Color can have a value that is a string of 3 or 4 element sequence.'''
    
    # What would happen if (0.6)*3 is used instead of (0.6,)*3?
    '''Error since (0.6)*3 is a float. The color takes a sequence with 3 elements for the RGB values.'''
    
    # What would happen if (0.3,)*3 is used instead of (0.6,)*3?
    '''It will be darker.'''
    
    # What would happen if (0.9,)*3 is used instead of (0.6,)*3?
    '''It will be lighter.'''
    
    plt.plot(x, fx2, color=(0.6,)*3, label='$f^{(2)}(x)$')
    plt.plot(x, fx4, 'k', label='$f^{(4)}(x)$')
    plt.legend(loc=0)
    # add axis labels
    plt.xlabel('$x$')
    plt.ylabel('$f(x)$')
    plt.show()
    
def plot_3_3(x0=0.3, r_min=0, r_max=1):
    # Add a docstring for this function. Parameters should be properly
    # documented and the docstring itself should follow the scipy/numpy
    # docstring convention and ReST format
    '''
    Make a Feigenbaum plot.
    
    Parameters
    ----------
    x0 : float
        Initial value for iteration.
    r_min : int or float
        Minimum value of the parameter constant
    r_max : int or float
        Maximum value of the parameter constant.   
    '''
    
    rs = np.linspace(r_min, r_max, 500)
    # What is the purpose of multiplying the output of np.ones() and a number?
    '''This makes an array full of the multiplied number with the same length as np.ones()'''
    
    # What are the dimensions of fxs?
    '''1001x500'''
    
    # What do the rows and columns of fxs represent?
    '''The rows represent the value of x_n while the columns represent each value of r in the the array rs.'''
    
    fxs = np.array(iterf(f, np.ones(len(rs))*0.3, rs, 1000))
    # What are the dimensions of fxs?
    '''1001x500'''
    
    # What does .T in the second argument do?
    '''It transposes the array.'''
    
    # Can we use fxs[100:,:] instead of fxs[100:,:].T? Why or why not?
    '''No since fxs[100:,:].T doesn't have the same dimension as rs.'''
    
    # What does the keyword ms do?
    '''It changes the marker size.'''
    
    plt.plot(rs, fxs[100:,:].T, 'k.', ms=2)
    # add axis labels
    plt.xlabel('$r$')
    plt.ylabel('$x$')
    plt.show()
    
def plot_3_4(x0=0.3):
    # Add a docstring for this function. Parameters should be properly
    # documented and the docstring itself should follow the scipy/numpy
    # docstring convention and ReST format
    '''
    Make a close-up of the Feigenbaum plot from r=0.88 to r=1.
    
    Parameters
    ----------
    x0 : float
        Initial value for iteration.
    r_min : int or float
        Minimum value of the parameter constant
    r_max : int or float
        Maximum value of the parameter constant.    
    '''
    plot_3_3(r_min=0.88)
    
def plot_3_5(x0=0.3, r = 0.934):
    # Add a docstring for this function. Parameters should be properly
    # documented and the docstring itself should follow the scipy/numpy
    # docstring convention and ReST format
    '''
    Plot the frequency distribution of x_n.
    
    Parameters
    ----------
    x0 : float
	    Initial value for iteration.
    r : float
	    Parameter constant in f.
    '''
    
    # Complete the following line
    fxs = iterf(f, x0, r, 400)
    plt.hist(fxs, bins=100)
    plt.xlim(xmin=0)
    # add axis labels
    plt.xlabel('$n$')
    plt.ylabel('frequency')
    plt.show()

def plot_3_6(x0=0.3, r=0.874640, maxiter=1000):
    # Add a docstring for this function. Parameters should be properly
    # documented and the docstring itself should follow the scipy/numpy
    # docstring convention and ReST format
    '''
    Plot the superstable four-cycle.
    
    Parameters
    ----------
    f : function
	    Function for iteration.
    x0 : float
	    Initial value for iteration.
    r : float
	    Parameter constant in f.
    maxiter : int
	    Maximum nuber of iteration.    
    '''
    
    xs = np.linspace(0, 1)
    fxs = iterf(f, x0, r, 1000)[100:]
    # complete the next two lines
    plt.plot(xs, xs)
    plt.plot(xs, f(xs,r))
    
    # What are the first 10 elements of the first argument of the ff. 
    # plt.plot() call?
    '''The first 10 elements are the first 5 elements of fxs.'''
    
    # Why was the last element of fxs omitted in the argument of np.repeat()?
    '''The last element of fxs was omitted in the argument of np.repeat() 
    because it is the last element of the iteration.
     It does not have a corresponding x_n since it is the last f(x_n).'''
    
    # Can we use fxs[:-1]*2 instead of np.repeat(fxs[:-1], 2)? Why or why not?
    '''No because fxs[:-1]*2 will repeat the entire list after the list while 
    np.repeat(fxs[:-1], 2) repeat evey element of fxs[:-1] after each element.'''
    
    plt.plot(np.repeat(fxs[:-1], 2), np.column_stack((fxs[:-1], fxs[1:])).ravel(), '-o')
    # What does the following argument of plt.plot() call represent?
    '''It draws the Cobweb plot for the logistic map.'''
    
    # What are the dimensions/shape of the following plt.plot() argument?
    '''1800'''
    
    # What are the dimensions of the argument of np.column_stack()?
    '''900 x 2'''
    
    # Why was the first element of fxs[1:] omitted?
    '''The first element of fxs[1:] omitted because it contains the intial value of iteration x_0.'''
    
    # What would happen if .ravel() is removed?
    '''There will be an  error since np.column_stack((fxs[:-1], fxs[1:])) does not the 
    same dimension as np.ravel(zip(fxs[:,1], fxs[1:]))'''
        
    # Can we use np.ravel(zip(fxs[:,1], fxs[1:])) instead of 
    # np.column_stack((fxs[:-1], fxs[1:])).ravel()? Why or why not?
    '''Yes because np.column_stack() does the same thing as zip() 
    except that the former returns an array while the latter returns a list. 
    The array or thelist is then ravelled'''
    
    # add axis labels
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.show()
    
def plot_3_7(x0=0.3, r=0.96420, maxiter=1000):
    # Add a docstring for this function. Parameters should be properly
    # documented and the docstring itself should follow the scipy/numpy
    # docstring convention and ReST format
    '''
    Plot the superstable four-cycle.
    
    Parameters
    ----------
    f : function
	    Function for iteration.
    x0 : float
	    Initial value for iteration.
    r : float
	    Parameter constant in f.
    maxiter : int
	    Maximum nuber of iteration.    
    '''
    
    # complete the following line
    plot_3_6(x0,r,maxiter)
    
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