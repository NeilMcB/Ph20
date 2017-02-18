import euler

#Directory for images
path = "images/"

#Q1
euler.trajectory_plot(0,1,0.01,10000,"Explicit",path+"Sec1Plt1.pdf")

#Q2
euler.error_plot(0,1,0.01,10000,"Explicit",path+"Sec1Plt2.pdf")

#Q3
euler.trunc_err(0,1,0.01,1000,"Explicit",path+"Sec1Plt3.pdf")

#Q4
euler.error_plot(0,1,0.01,10000,"Explicit",path+"Sec1Plt4.pdf",E_plot=True)

#Q5
euler.error_plot(0,1,0.01,10000,"Implicit",path+"Sec1Plt5.pdf",E_plot=True)

#Q6
euler.phase_space(0,1,0.01,1000,["Implicit","Explicit"],path+"Sec2Plt1.pdf")

#Q7
euler.phase_space(0,1,0.2,500,["Symplectic"],path+"Sec2Plt2.pdf")

#Q8
euler.error_plot(0,1,0.01,10000,"Symplectic",path+"Sec2Plt3.pdf",E_plot=True)

#Q9
euler.phase_lag(0,1,0.2,500,path+"Sec2Plt4.pdf")