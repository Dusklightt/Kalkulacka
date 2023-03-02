.PHONY: all run profile clean pack
EXECUTABLE = calculator
MAIN = main.py
PROF = profiling.py

all: $(EXECUTABLE)

$(EXECUTABLE): $(MAIN)
	python $<

run: $(MAIN)
	python $<

profile: $(PROF)
	python $<

$(PROF): $(MAIN)
	python $<
pack:
	cd .. && cd .. && mkdir repo && xcopy IVS-Project repo /S /H
	cd .. && cd .. && tar -cf xkubov08_xstafl01_xvalac13_xvasut02.gzip repo doc install

clean:
	cd __pycache__ && del *.pyc
	rmdir __pycache__