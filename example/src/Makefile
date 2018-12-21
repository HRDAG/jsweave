# Authors:     SL
# Maintainers: SL
# License: 	   2018, HRDAG, GPL v2 or later
# ============================================
# jsweave/test/data/example/src/Makefile

.PHONY: all clean

all: output/example.pdf		

clean:
	-rm output/*

output/example.pdf: \
		src/example.tex \
		src/json.json  
		pdflatex src/example.tex
		mv example.pdf output/example.pdf 
		mv example.log output/example.log 	
		mv example.aux output/example.aux
#done.
