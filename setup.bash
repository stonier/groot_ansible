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
  fi
fi
# Always pulling for now
python setup.py develop

echo ""
echo "Leave the virtual environment with 'deactivate'"
echo ""
echo "I'm grooty, you should be too."
echo ""

