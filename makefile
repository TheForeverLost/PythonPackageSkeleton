
init:
	pip install -r requirements.txt
	python setup.py install

test:
	pytest tests

dist:
	python setup.py sdist
	python setup.py bdist_wheel

deploy:
	python3 -m pip install --user --upgrade twine && python3 -m twine upload dist/*

testdeploy:
	python3 -m pip install --user --upgrade twine && python3 -m twine upload --repository testpypi dist/*
