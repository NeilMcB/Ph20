#!python/usr/bin

import numpy as np
import matplotlib.pyplot as plt

#A function to plot X = A_x*cos(2pi*f_x*t)
#                   Y = A_y*sin(2pi*f_y*t + phi)
#                   Z = x + y
#Each plot is stored as a separate txt file.
def calc_plots(A_x, A_y, f_x, f_y, phi, dt, N):
    #Generate time-scale
    t = np.arange(0, N*dt, dt)

    #Generate the functions
    X = A_x*np.cos(2*np.pi*f_x*t)
    Y = A_y*np.sin(2*np.pi*f_y*t + phi)
    Z = X + Y

    #Store as seperate files
    np.savetxt("out_X.txt", X)
    np.savetxt("out_Y.txt", Y)
    np.savetxt("out_Z.txt", Z)
    np.savetxt("out_t.txt", t)

#A function to perform repeated plots of X vs Y
#for a specified range of frequencies
def ratio_plots(A_x, A_y, f_xs, f_ys, phi, dt, N):
    #Initialise plot for graphing
    fig, ax = plt.subplots(nrows=1, ncols=1)

    #Create plot for each f_x and f_y
    for f_x in f_xs:
        for f_y in f_ys:
            #Determine function for given frequencies
            calc_plots(A_x, A_y, f_x, f_y, phi, dt, N)

            #Add current ratio to plot
            X = np.loadtxt("out_X.txt")
            Y = np.loadtxt("out_Y.txt")
            
            label = "f_x/f_y = {:f}".format(float(f_x)/float(f_y))

            ax.plot(X, Y, label=label)

    #Make the plot pretty :)
    A_max = max(A_x, A_y)
    fig.subplots_adjust(left=-0.1)
    ax.set_xlim([-1*A_max, A_max])
    ax.set_ylim([-1*A_max, A_max])
    ax.set_aspect("equal")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("X vs Y for varied f_x/f_y")
    ax.legend(bbox_to_anchor=(1.5,1.05))

    #Save the plot
    fig.savefig("fxfy_ratio.pdf")
    plt.close(fig)


#A function to perform repeated plots of X xs Y
#for f_x = f_y and varied phi
def phi_plots(A_x, A_y, f_x, f_y, phis, dt, N):
    #Initialise plot for graphing
    fig, ax = plt.subplots(nrows=1, ncols=1)

    #Create plot for each f_x and f_y
    for phi in phis:
        #Determine function for given phase
        calc_plots(A_x, A_y, f_x, f_y, phi, dt, N)

        #Add current phase to plot
        X = np.loadtxt("out_X.txt")
        Y = np.loadtxt("out_Y.txt")
        
        label = "phi = {:f}".format(float(phi))
        
        ax.plot(X, Y, label=label)

    #Make the plot pretty :)
    A_max = max(A_x, A_y)
    fig.subplots_adjust(left=-0.1)
    ax.set_xlim([-1*A_max, A_max])
    ax.set_ylim([-1*A_max, A_max])
    ax.set_aspect("equal")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("X vs Y for varied phi")
    ax.legend(bbox_to_anchor=(1.5,1.05))

    #Save the plot
    fig.savefig("phi_var.pdf")
    plt.close(fig)


#A function to perform plot a beat wave given
#similar f_x, f_y
def beat_plot(A_x, A_y, f_x, f_y, phi, dt, N):
    #Initialise plot for graphing
    fig, ax = plt.subplots(nrows=1, ncols=1)

    #Determine function for given frequencies
    calc_plots(A_x, A_y, f_x, f_y, phi, dt, N)
    
    #Plot
    Z = np.loadtxt("out_Z.txt")
    t = np.loadtxt("out_t.txt")
    ax.plot(t, Z)

    #Make the plot pretty :)
    ax.set_xlabel("t")
    ax.set_ylabel("Z")
    ax.set_title("Z = X + Y beat wave: f_x/f_y = {:f}"
                 .format(float(f_x)/float(f_y)))

    #Save the plot
    fig.savefig("beat_wave.pdf")
    plt.close(fig)
