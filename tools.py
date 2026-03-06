import numpy as np
import matplotlib.pyplot as plt

def plot_many(y_axis,funcs,title='',xlab='',ylab=''):
    '''Несколько графиков'''
    
    plt.figure()
    for idx, f in enumerate(funcs):
        plt.plot(y_axis, f, label=f"x{idx+1}(t)")
        
    plt.grid(True)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.show()
    
def plot_many_xlim(y_axis,funcs,title='',xlab='',ylab=''):
    '''Несколько графиков'''
    
    plt.figure()
    for idx, f in enumerate(funcs):
        plt.plot(y_axis, f, label=f"x{idx+1}(t)")
        
    plt.grid(True)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.ylim(-1,1)
    plt.show()
def matrix(lists):
     return np.array(lists, dtype = float)
