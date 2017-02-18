#Makefile

#Generates report with updated images
Ph20_Lab4.pdf : images/Sec1Plt1.pdf Euler_code.tex Ph20_Lab4.tex
	pdflatex Ph20_Lab4.tex
	pdflatex Ph20_Lab4.tex

#Generates images only
images/Sec1Plt1.pdf : ass4.py euler.py
	python ass4.py

#Generates code pdf only
Euler_code.pdf : ass4.py euler.py
	pdflatex Euler_code.tex

.PHONY : clean
clean : 
	rm -f images/*
	rm -f *.aux
	rm -f *.log
