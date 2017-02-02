#!/bin/bash

# Script for setting up the development environment.
PROJECT=groot_ansible

if [ "${VIRTUAL_ENV}" == "" ]; then
  workon ${PROJECT}
  if [ $? -ne 0 ]; then
    mkvirtualenv ${PROJECT}
    if [ $? -ne 0 ]; then
    	sudo apt-get install virtualenvwrapper
        mkvirtualenv ${PROJECT}
    fi
    # hack used by a badly installing ansible->cffi pip install in the virtual env requirements
    sudo apt install libffi-dev
    # probably some python setup.py target which will do this for you
    pip install vcs_extras
  fi
fi
# Always pulling for now
python setup.py develop

echo ""
echo "Leave the virtual environment with 'deactivate'"
echo ""
echo "I'm grooty, you should be too."
echo ""

