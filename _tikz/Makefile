ITEMS=$(wildcard *.tex)

../images/%.svg: ./%.tex
	pdflatex -shell-escape $(^) && $(RM) *.log *.aux
	pdf2svg $(patsubst %.tex,%.pdf,$(^)) $(@)

.PHONY: all clean
all: $(patsubst %.tex,%.svg,$(addprefix ../images/, $(ITEMS)))
	${RM} *.pdf

clean:
	$(RM) *.log *.aux *.pdf *.svg

