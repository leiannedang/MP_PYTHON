# -*- coding: utf-8 -*-
"""

Machine Problem 3 (Python Solution)
By Group 1 of 2ECE-A
Michael Jeffrey Carlos and Lei-Ann Edang

This program accepts experimental points (x,y) from 1st to 10th degree
and returns the coefficients of the polynomial f(x) that best 
approximates the data based on its least norm of error vector e(x). It
should be noted that the points are in the form of an nx2 matrix.

"""

import numpy as np

print("Input Experimental Points [[xi], [yi]]: ")
Z = eval(input())

#Setting arrays to a single dimension
xi = np.array([Z[0]])
xi = xi.flatten()

yi = np.array([Z[1]])
yi = yi.flatten()

#Computing the Line of Best Fit
"""
Variables:
    p = regression analysis
    g = polynomial function
    e = error
    n = norm of error
"""
    
#degree 1
p1 = np.polyfit(xi, yi, 1)
g1 = np.polyval(p1, xi)
e1 = yi - g1
n1 = np.linalg.norm(e1)

#degree 2
p2 = np.polyfit(xi, yi, 2)
g2 = np.polyval(p2, xi)
e2 = yi - g2
n2 = np.linalg.norm(e2)

#degree 3
p3 = np.polyfit(xi, yi, 3)
g3 = np.polyval(p3, xi)
e3 = yi - g3
n3 = np.linalg.norm(e3)

#degree 4
p4 = np.polyfit(xi, yi, 4)
g4 = np.polyval(p4, xi)
e4 = yi - g4
n4 = np.linalg.norm(e4)

#degree 5
p5 = np.polyfit(xi, yi, 5)
g5 = np.polyval(p5, xi)
e5 = yi - g5
n5 = np.linalg.norm(e5)

#degree 6
p6 = np.polyfit(xi, yi, 6)
g6 = np.polyval(p6, xi)
e6 = yi - g6
n6 = np.linalg.norm(e6)

#degree 7
p7 = np.polyfit(xi, yi, 7)
g7 = np.polyval(p7, xi)
e7 = yi - g7
n7 = np.linalg.norm(e7)

#degree 8
p8 = np.polyfit(xi, yi, 8)
g8 = np.polyval(p8, xi)
e8 = yi - g8
n8 = np.linalg.norm(e8)

#degree 9
p9 = np.polyfit(xi, yi, 9)
g9 = np.polyval(p9, xi)
e9 = yi - g9
n9 = np.linalg.norm(e9)

#degree 10
p10 = np.polyfit(xi, yi, 10)
g10 = np.polyval(p10, xi)
e10 = yi - g10
n10 = np.linalg.norm(e10)

#Compiling the norms of the 1st up to the 10th degree
e_list = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]
e_array = np.array([e_list])
n_vector = np.min(e_array)

#Displaying the coefficients of the best approximate of f(x) 
if (n_vector == n1):
    print("The coefficients the 1st Degree Polynomial are: ")
    print(p1)
    
elif (n_vector == n2):
    print("The coefficients the 2nd Degree Polynomial are: ")
    print(p2)
    
elif (n_vector == n3):
    print("The coefficients the 3rd Degree Polynomial are: ")
    print(p3)
    
elif (n_vector == n4):
    print("The coefficients the 4th Degree Polynomial are: ")
    print(p4)
    
elif (n_vector == n5):
    print("The coefficients the 5th Degree Polynomial are: ")
    print(p5)
    
elif (n_vector == n6):
    print("The coefficients the 6th Degree Polynomial are: ")
    print(p6)
    
elif (n_vector == n7):
    print("The coefficients the 7th Degree Polynomial are: ")
    print(p7)

elif (n_vector == n8):
    print("The coefficients the 8th Degree Polynomial are: ")
    print(p8)
    
elif (n_vector == n9):
    print("The coefficients the 9th Degree Polynomial are: ")
    print(p9)

elif (n_vector == n10):
    print("The coefficients the 10th Degree Polynomial are: ")
    print(p10)

else:
    print("Error! Limit not satisfied.")
    
