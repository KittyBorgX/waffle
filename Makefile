init:
	pip install -r requirements.txt

test:
	py.test tests

run:
	python waffle/waffle.py

.PHONY: init test run

