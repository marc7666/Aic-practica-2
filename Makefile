test:
	python3 backtracking.py
	python3 backtracking_rec.py
	python3 dynamic_programming.py
	python3 greedy.py
	python3 greedy_rec.py

all:
	pylint arbol.py
	pylint backtracking.py
	pylint backtracking_rec.py
	pylint calculs.py
	pylint dynamic_programming.py
	pylint greedy.py
	pylint read_file.py
	pylint greedy_rec.py
