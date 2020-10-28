all: phd-thesis

phd-thesis: phd-thesis.pdf

phd-thesis.pdf: phd-thesis.tex chapters/*.tex
	export TEXINPUTS=.:./texmf/:
	mkdir -p output
	pdflatex -output-directory output/ phd-thesis.tex
	bibtex output/phd-thesis.aux
	pdflatex -output-directory output/ phd-thesis.tex
	pdflatex -output-directory output/ phd-thesis.tex
	mv output/phd-thesis.pdf ./
	rm -r output

clean:
	rm phd-thesis.pdf
