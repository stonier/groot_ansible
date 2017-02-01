#
# License: BSD
#    https://raw.githubusercontent.com/stonier/groot_ansible/devel/LICENSE
#
##############################################################################
# Documentation
##############################################################################

"""
Ansible subcommands for ros management.
"""

##############################################################################
# Imports
##############################################################################

import argparse
import subprocess

from . import common
from . import console

##############################################################################
# Methods
##############################################################################


def parse_args(args):
    """
    Updates ansible
    """
    console.banner("'update'")
    connection = "-c local"
    list_tasks = "--list-tasks" if args.list_tasks else ""
    cmd = "ansible-playbook update.yaml -K -i localhost, {connection} {list_tasks}".format(**locals())
    cmd = common.append_verbosity_argument(cmd, args.verbose)
    console.key_value_pairs("Ansible", {"Command": cmd}, 10)
    print("")
    subprocess.call(cmd, cwd=args.home, shell=True)


def add_subparser(subparsers):
    """
    Add our own argparser to the parent.

    :param subparsers: the subparsers factory from the parent argparser.
    """
    parser = subparsers.add_parser("update",
                                   description="Update apt and the groot_ansible ecosystem",  # this shows in the help for this command
                                   help="update your ansible/apt environment",  # this shows in the parent parser
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter
                                   )
    common.add_ansible_arguments(parser)
    parser.set_defaults(func=parse_args)
