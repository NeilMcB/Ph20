#Makefile
plots = images/Sec1Plt1.pdf images/Sec1Plt2.pdf images/Sec1Plt3.pdf images/Sec1Plt4.pdf images/Sec1Plt5.pdf images/Sec2Plt1.pdf images/Sec2Plt2.pdf images/Sec2Plt3.pdf images/Sec2Plt4.pdf

#Generates report with updated images
Ph20_Lab4.pdf : Ph20_Lab4.tex $(plots) Euler_code.pdf 
	pdflatex $<

#Generates images only
%.pdf : ass4.py euler.py
	python $< $@

#Generates code pdf only
Euler_code.pdf : ass4.py euler.py
	pdflatex Euler_code.tex

.PHONY : clean
clean : 
	rm -f images/*
	rm -f *.aux
	rm -f *.log
