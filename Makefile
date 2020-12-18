install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

test:
	python -m pytest -vv tests/*.py