# make a folder for each new aoc day - each folder contains a python file and an input file

value ?= test_folder

.PHONY: folder

folder:
	@echo "Building folder for: $(value)"

	@mkdir $(value)
	@touch $(value)/$(value).py
	@touch $(value)/input.txt
