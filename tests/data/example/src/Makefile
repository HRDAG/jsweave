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
		src/example.Rmd \
		#src/example_json.json  
		Rscript -e rmarkdown::render"("src/example.Rmd", output_format = "all")"
#done.
