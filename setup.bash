#!/bin/bash

# Script for setting up the development environment.

PROJECT=groot_ansible

###########################
# Colours
###########################

BOLD="\e[1m"

CYAN="\e[36m"
GREEN="\e[32m"
RED="\e[31m"
YELLOW="\e[33m"

RESET="\e[0m"

#############################
# Functions
#############################

padded_message ()
{
  line="........................................"
  printf "%s %s${2}\n" ${1} "${line:${#1}}"
}

pretty_header ()
{
  echo -e "${BOLD}${1}${RESET}"
}

pretty_print ()
{
  echo -e "${GREEN}${1}${RESET}"
}

pretty_warning ()
{
  echo -e "${YELLOW}${1}${RESET}"
}

pretty_error ()
{
  echo -e "${RED}${1}${RESET}"
}

# smart installer that doesn't call sudo if it doesn't need to
install_package ()
{
  PACKAGE_NAME=$1
  dpkg -s ${PACKAGE_NAME} > /dev/null
  if [ $? -ne 0 ]; then
    sudo apt-get -q -y install ${PACKAGE_NAME} > /dev/null
  else
    pretty_print "  $(padded_message ${PACKAGE_NAME} "found")"
    return 0
  fi
  if [ $? -ne 0 ]; then
    pretty_error "  $(padded_message ${PACKAGE_NAME} "failed")"
    return 1
  fi
  pretty_warning "  $(padded_message ${PACKAGE_NAME} "installed")"
  return 0
}

#############################
# System Dependencies
#############################

pretty_header "Dependencies"

install_package virtualenvwrapper || return
install_package python-setuptools || return
install_package libyaml-dev || return
install_package libpython2.7-dev || return

# in case virtualenvwrapper was just installed, re-source your environment to get the bash function mkvirtualenv
. ~/.profile

#############################
# Virtual Env
#############################

if [ "${VIRTUAL_ENV}" == "" ]; then
  workon ${PROJECT}
  if [ $? -ne 0 ]; then
    mkvirtualenv ${PROJECT}
  fi
fi

#############################
# Setup Groot Ansible
#############################

python setup.py develop

echo ""
echo "Leave the virtual environment with 'deactivate'"
echo ""
echo "I'm grooty, you should be too."
echo ""

