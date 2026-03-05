import numpy as np
import matplotlib.pyplot as plt

def plot_many(time,funcs,title=''):
    '''Несколько графиков'''
    
    plt.figure()
    for idx, f in enumerate(funcs):
        plt.plot(time, f, label=f"x{idx+1}(t)")
        
    plt.grid(True)
    plt.xlabel('t, с')
    plt.ylabel('x(t)')
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.show()

