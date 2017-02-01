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

import argparse
import functools
import os
import subprocess

from . import console

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
# Generic Playbook to Subcommand
##############################################################################


def execute_generic_subcommand(name, become_sudo, args):
    """
    :param str name: name of the subcommand and playbook yaml
    :param bool become_sudo: whether to run as sudo or not

    """
    console.banner("'{0}'".format(name))
    connection = "-c local"
    list_tasks = "--list-tasks" if args.list_tasks else ""
    sudo_command = "-K" if become_sudo else ""
    cmd = "ansible-playbook {name}.yaml {sudo_command} -i localhost, {connection} {list_tasks}".format(**locals())
    cmd = append_verbosity_argument(cmd, args.verbose)
    console.key_value_pairs("Ansible", {"Command": cmd}, 10)
    print("")
    subprocess.call(cmd, cwd=args.home, shell=True)


def add_generic_subparser(subparsers, name, short_description, description, become_sudo):
    """
    Create a generic subparser which runs a playbook directly.

    :param subparsers: the subparsers factory from the parent argparser
    :param str name: name of the subcommand and playbook yaml
    :param str short_description: subcommand help string (shows in the parent parser)
    :param str description: full subcommand description (shows in --help for this subcommand)
    :param bool become_sudo: whether to run as sudo or not
    """
    parser = subparsers.add_parser(name,
                                   help=short_description,
                                   description=description,
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter
                                   )
    add_ansible_arguments(parser)
    parser.set_defaults(func=functools.partial(execute_generic_subcommand, name, become_sudo))


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


def add_apt_arguments(parser):
    """
    Any arguments for the parser related to apt management.

    :param argparse.ArgumentParser parser:
    """
    group = parser.add_argument_group(title="apt arguments")
    group.add_argument('-s', '--skip-apt-update', action='store_true', help='skip an update of the apt cache')
