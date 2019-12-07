# -*- coding: utf-8 -*-
"""

Machine Problem 4 (Python Solution)
By Group 1 of 2ECE-A
Michael Jeffrey Carlos and Lei-Ann Edang

ProjMotion Function accepts values for the constant-velocity motion in the 
horizontal direction and free-fall motion in the vertical direction such 
as the initial height, magnitude of the velocity, angle in degrees, as 
well as the x and y components of the acceleration. Afterwards, it will 
return the plot for its trajectory or its projectile motion.

"""

import matplotlib.pyplot as plt
import math as math

def ProjMotion(H, V, Theta, Ax, Ay):
    
    """
    Variables:
        H - initial height above the ground 
        V = magnitude of the velocity 
        Theta - angle wrt x-axis
        Ax - x-component of acceleration
        Ay - y-component of acceleration
    """
    
    #Detection of Error Input 
    if Ay == 0:
        error = 'Invalid Input! No Free Fall!'
        print(error)
        return
    
    #Computing the Components of Velocity
    Vx = V * math.cos(Theta * ((math.pi) / 180))
    Vy = V * math.sin(Theta * ((math.pi) / 180))
    
    #Applying Equation 2
    
    X = []
    Y = []
    
    t = 0 #time
    d = 1/1000 #displacement
    Xi = 0
    Yi = H
    
    X.append(Xi)
    Y.append(H)
    
    while(Yi > d):
        
        t += d
        
        Xi = (Vx * t) + ((1/2) * Ax * (t**2))
        Yi = (Vy * t) + ((1/2) * Ay * (t**2)) + H
        
        X.append(Xi)
        Y.append(Yi)
        
        if Yi < d:
            break
    
    #Plotting the Graph of the Motion
    plt.plot(X,Y, 'm--', linewidth = 3.0)
    
    #Modifying the Graph of the Motion
    plt.title('Trajectory of the Projectile Motion')
    plt.ylabel('Displacement in the Y-coordinate')
    plt.xlabel('Displacement in the X-coordinate')

    #Displaying the Graph
    plt.show()
    
    
    
        