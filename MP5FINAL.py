# -*- coding: utf-8 -*-
"""

Machine Problem 5 (Python Solution)
By Group 1 of 2ECE-A
Michael Jeffrey Carlos and Lei-Ann Edang

XFunction Function accepts a function of x(n) to determine the value of 
y(n) depending on which piecewise function it satisfies. It will also
return the superimposed graphs of both functions.

"""

import numpy as np # for np user-input functions
import matplotlib.pyplot as plt

n = np.linspace(0,199,200)

# Defining the function of x 
def XFunction(x):
    
    y = np.zeros(200)

# Defining the function of y    
    for j in n:
        
        j = int(j)
        
        if j == 0:
            y[j] = -1.5*x[j] + 2*x[j+1] - 0.5*x[j+2] # Condition 1
            
        elif j > 0 and j <= 198:
            y[j] = 0.5*x[j+1] - 0.5*x[j-1] # Condition 2
            
        elif j == 199:
            y[j] = 1.5*x[j] - 2*x[j-1] + 0.5*x[j-2] # Condition 3
    
#Plotting the functions    
    plt.plot(list(range(0,200)), x, '--b', label = 'Function of x')
    plt.plot(list(range(0,200)), y, '-r', label = 'Function of y')

#Customizing the Graphs
    plt.legend(frameon = True, loc = 'lower center')
    plt.ylabel('Value of y(n)')
    plt.xlabel('Value of x(n)')
    plt.title('Graphs of x(n) and y(n)')

#Displaying the Graphs
    plt.show()
    