# Authors:     SL
# Maintainers: SL
# License: 	   2018, HRDAG, GPL v2 or later
# ============================================
# jsweave/test/data/example/src/Makefile

.PHONY: all clean

all: output/example_workflow.pdf		

clean:
	-rm output/*

output/example_workflow.pdf: \
		src/example.tex \
		src/json.json  
		pdflatex example.tex
	#cd src && pdflatex dcjs-cja-report-processed.tex
#done.
