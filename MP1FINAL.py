# -*- coding: utf-8 -*-
"""

Machine Problem 1 (Python Solution)
By Group 1 of 2ECE-A
Michael Jeffrey Carlos and Lei-Ann Edang

function(n) Function implements given piecewise functions where 
n is an integer greater than or equal to zero. In the same way, after
computing for the specific values of the function, this program graphs
f(n) from n = 0 and n = 99 using the stem command.

"""

import matplotlib.pyplot as plt
import numpy as np

def function(n):
    
#Setting the piecewise equations
    q = np.multiply(n,n)
    ans = q - 7
    
#Case 1; n is less than 9
    while(n < 10):
        return ans
    return function(n - 10)

#Case 2; n is greater than or equal to 10
x = []
y = []
        
for i in range(0,100):    
    x.append(i)
    y.append(function(i))
    
#Plotting the Points
plt.stem(x,y, linefmt = 'grey', use_line_collection = True)

#Labelling the Figure    
plt.title('Graph of function(n)')
plt.ylabel('Y-Axis (function(n))')
plt.xlabel('X-Axis (n)')
    
#Displaying the Figure
plt.show()
