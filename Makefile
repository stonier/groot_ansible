VERSION=`./setup.py --version`

help:
	@echo "Local Build"
	@echo "  build     : build the python package."
	@echo "Packages"
	@echo "  pypi      : upload the package to PyPI."
	@echo "  source_deb: source packaging (for ppas)"
	@echo "  deb       : build the deb."
	@echo "  upload_deb: upload to yujin's repository."
	@echo "  release   : make pypi (if open), deb and upload together."
	@echo "Other"
	@echo "  build_deps: install various build dependencies."
	@echo "  clean     : clean build/dist directories."

build:
	python setup.py build

build_deps:
	echo "Downloading dependencies"
	sudo apt-get install python-stdeb virtualenvwrapper

clean:
	-rm -f MANIFEST
	-rm -rf build dist
	-rm -rf deb_dist
	-rm -rf debian
	-rm -rf ../*.build
	-rm -rf *.tar.gz
	-rm -rf *.egg-info

source_package:
	python setup.py sdist

source_deb:
	rm -rf dist deb_dist
	python setup.py --command-packages=stdeb.command sdist_dsc

deb:
	rm -rf dist deb_dist
	python setup.py --command-packages=stdeb.command bdist_deb

pypi: 
	python setup.py sdist bdist_wheel
	twine upload dist/*

pypi_test:
	python setup.py sdist bdist_wheel
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

release: pypi deb

