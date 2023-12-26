# make a folder for each new aoc day - each folder contains a python file and an input file

value ?= test_folder

.PHONY: folder

folder:
	@echo "Building folder for: $(value)"

	@mkdir $(value)
	@touch $(value)/$(value).py
	@echo "#data = open(<INPUT_FILE>, 'r').read().split('\n')" >> $(value)/$(value).py
	@touch $(value)/input1.txt
	@touch $(value)/input2.txt
