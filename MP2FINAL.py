# -*- coding: utf-8 -*-
"""

Machine Problem 2 (Python Solution)
By Group 1 of 2ECE-A
Michael Jeffrey Carlos and Lei-Ann Edang

Circle function accepts three input points (x,y) lying on a circle in a 
2-dimensional Cartesian Plane. From this set of points, it will return 
the values of the center (h,k) and radius (r) of the circle as well as
the coefficients of the general equation of the circle in the form of 
vector ([D E F]).

"""

import numpy as np

def Circle(x1, x2, x3, y1, y2, y3):
    
    import math as math
    
    #Forming the Equation of a Circle
    Circle1 = x1**2 + y1**2
    Circle2 = x2**2 + y2**2
    Circle3 = x3**2 + y3**2
    
    #Creating the Matrix
    matA = np.array([(x1, y1, 1), 
                     (x2, y2, 1), 
                     (x3, y3, 1)])
    
    matD = -np.array([(Circle1, y1, 1), 
                      (Circle2, y2, 1), 
                      (Circle3, y3, 1)])
    
    matE = np.array([(Circle1, x1, 1), 
                     (Circle2, x2, 1), 
                     (Circle3, x3, 1)])
    
    matF = -np.array([(Circle1, x1, y1), 
                      (Circle2, x2, y2), 
                      (Circle3, x3, y3)]) 
    
    #Solving for the vector [D, E, F] of a Circle
    detA = np.linalg.det(matA)
    
    detD = np.linalg.det(matD)
    detE = np.linalg.det(matE)
    detF = np.linalg.det(matF)
    
    ValD = np.divide(detD, detA)
    ValE = np.divide(detE, detA)
    ValF = np.divide(detF, detA)
    
    rnd_ValD = ValD.astype(int)
    rnd_ValE = ValE.astype(int)
    rnd_ValF = ValF.astype(int)
    
    #Solving for the center point (h, k) of a Circle
    Denom = np.multiply(2, detA)
    h = -np.divide(detD, Denom)
    k = -np.divide(detE, Denom)
    
    around_h = h.astype(int)
    around_k = k.astype(int)
    
    #Solving for the radius of a Circle
    hx2 = (h - x1)**2
    ky2 = (k - y1)**2
    r = math.sqrt(hx2 + ky2)
    
    around_r = np.around(r, decimals = 2)
    
    #Printing the Results
    print('Parameters of the Circle on which the three points lie: ')
    print('Center (h,k): (', around_h, ',', around_k, ')')
    print('Radius (r): ', around_r)
    print('Vector [D, E, F]: [', rnd_ValD, ',', rnd_ValE, ',', rnd_ValF,']')
    print('\n')
    
    #Standard and General Equations of a Circle
    print('Standard Equation of the Circle: ')
    print('( x -', around_h, ')^2 + ( y - ', around_k,')^2')
    print('\n')
    print('General Equation of the Circle: ')
    print('x^2 + y^2 +', rnd_ValD, 'x +', rnd_ValE, 'y +', rnd_ValF, '= 0')
    
    
    
    
    