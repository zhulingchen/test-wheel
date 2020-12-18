install:
	pip install --upgrade pip &&\
	pip install setuptools wheel &&\
	pip install -r requirements.txt

test:
	python -m pytest -vv tests/*.py

package:
	python setup.py sdist bdist_wheel