
test:
	make test_iterative
	make test_recursive

test_iterative:
	python3 ....

test_recursive:
	python3 ....

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
