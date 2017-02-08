#!/usr/bin/python

import numpy as np

#A function to print an entire list to a file
#Format reflects np.savetxt
def print_list(items, location):
    for item in items:
        location.write("%s\n" % item)

#A fucntion to plot X = A_x*cos(2pi*f_x*t)
#                   Y = A_y*sin(2pi*f_y*t + phi)
#                   Z = x + y
#Each plot is stored as a separate txt file
def calc_plots(A_x, A_y, f_x, f_y, phi, dt, N):
    #Initialise empty lists to store functions
    X = []
    Y = []
    Z = []
    
    #Perform calculation at each step in time
    t = 0
    for i in range(N):
        x = A_x * np.cos(2*np.pi*f_x*t)
        y = A_y * np.sin(2*np.pi*f_y*t + phi)
        z = x + y
        #Increment time
        t += dt
        #Store in function list
        X.append(x)
        Y.append(y)
        Z.append(z)

    #Print the function lists to file
    x_file = open("out_X.txt", 'w')
    print_list(X, x_file)
    x_file.close()

    y_file = open("out_Y.txt", 'w')
    print_list(Y, y_file)
    y_file.close()
    
    z_file = open("out_Z.txt", 'w')
    print_list(Z, z_file)
    z_file.close()

