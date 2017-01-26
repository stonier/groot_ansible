#
# License: BSD
#    https://raw.githubusercontent.com/stonier/groot_ansible/devel/LICENSE
#
##############################################################################
# Documentation
##############################################################################

"""
Common methods.
"""

##############################################################################
# Imports
##############################################################################

import os

##############################################################################
# Methods
##############################################################################


def get_playbook_home():
    # This package is already imported and has a file attribute.  Use that.
    return os.path.abspath(os.path.join(os.path.dirname(__file__), 'playbooks'))

##############################################################################
# Ansible Command Formatting
##############################################################################


def append_verbosity_argument(cmd, verbosity):
    """
    Just in case we want to modify how many v's we use, centralise this here.
    """
    return cmd + " -vvvv" if verbosity else cmd

##############################################################################
# Argument Parsing
##############################################################################


def add_ansible_arguments(parser):
    """
    Any arguments for the parser that should be available for every single
    ansible call.

    :param argparse.ArgumentParser parser:
    """
    group = parser.add_argument_group(title="ansible arguments")
    group.add_argument('-v', '--verbose', action='store_true', help='execute the playbook with extra verbosity')
    group.add_argument('--home', action='store', default=get_playbook_home(), help='path to the groot-ansible playbooks home')
    group.add_argument('--list-tasks', action='store_true', default=False, help='ansible will list the task that would be executed by this playbook')


def add_ros_arguments(parser):
    """
    Arguments relevant for a ros system.

    :param argparse.ArgumentParser parser:
    """
    group = parser.add_argument_group(title="ros arguments")
    group.add_argument('--only-upgrade', action='store_true', help='only upgrade currently installed ros debians')
    group.add_argument('--only-rosdeps', action='store_true', help='only do the --install-rosdeps step')
    group.add_argument('--skip-rosdeps', action='store_true', help='skip the --install-rosdeps step')
