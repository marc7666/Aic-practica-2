
test:
	make test_iterative
	make test_recursive

test_iterative:
	python3 backtracking.py
	python3 dynamic_programming.py
	python3 greedy.py

test_recursive:
	python3 backtracking_rec.py
	python3 dynamic_programming_rec.py
	python3 greedy_rec.py

lint:
	pylint arbol.py
	pylint backtracking.py
	pylint backtracking_rec.py
	pylint dynamic_programming.py
	pylint greedy.py
	pylint read_file.py
	pylint greedy_rec.py
	pylint calculs.py
	pylint dynamic_programming_rec.py
	pylint ejecutrar_test.py

all:
	make lint
	make test
