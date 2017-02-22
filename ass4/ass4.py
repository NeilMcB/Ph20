import euler
import sys

filename = sys.argv[1]

#Directory for images
path = "images/"
file = ".pdf"

if  (filename==path+"Sec1Plt1.pdf"):
	#Q1
	euler.trajectory_plot(0,1,0.01,10000,"Explicit",filename)
elif(filename==path+"Sec1Plt2.pdf"):
	#Q2
	euler.error_plot(0,1,0.01,10000,"Explicit",filename)
elif(filename==path+"Sec1Plt3.pdf"):
	#Q3
	euler.trunc_err(0,1,0.01,1000,"Explicit",filename)
elif(filename==path+"Sec1Plt4.pdf"):
	#Q4
	euler.error_plot(0,1,0.01,10000,"Explicit",filename,E_plot=True)
elif(filename==path+"Sec1Plt5.pdf"):
	#Q5
	euler.error_plot(0,1,0.01,10000,"Implicit",filename,E_plot=True)
elif(filename==path+"Sec2Plt1.pdf"):
	#Q6
	euler.phase_space(0,1,0.01,1000,["Implicit","Explicit"],filename)
elif(filename==path+"Sec2Plt2.pdf"):
	#Q7
	euler.phase_space(0,1,0.2,500,["Symplectic"],filename)
elif(filename==path+"Sec2Plt3.pdf"):
	#Q8
	euler.error_plot(0,1,0.01,10000,"Symplectic",filename,E_plot=True)
elif(filename==path+"Sec2Plt4.pdf"):
	#Q9
	euler.phase_lag(0,1,0.2,500,filename)