#
# License: BSD
#    https://raw.githubusercontent.com/stonier/groot_ansible/devel/LICENSE
#
##############################################################################
# Documentation
##############################################################################

"""
Subcommand for chrome installation
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
    Argument subparsing for this command.

    :param args: args resulting from the argparse module instantiation
    """
    console.banner("'chrome'")
    connection = "-c local"
    list_tasks = "--list-tasks" if args.list_tasks else ""
    # rosdistro = args.rosdistro if args.rosdistro else ros.guess_rosdistro()
    variables = "-e apt_update=false" if args.skip_apt_update else "-e apt_update=true"
    cmd = "ansible-playbook chrome.yaml -K -i localhost, {connection} {list_tasks} {variables}".format(**locals())
    cmd = common.append_verbosity_argument(cmd, args.verbose)
    console.key_value_pairs("Ansible", {"Command": cmd}, 10)
    print("")
    subprocess.call(cmd, cwd=args.home, shell=True)


def add_subparser(subparsers):
    """
    Add our own argparser to the parent.

    :param subparsers: the subparsers factory from the parent argparser.
    """
    parser = subparsers.add_parser("chrome",
                                   description="Google chrome setup/install/update",  # this shows in the help for this command
                                   help="google chrome for ubuntu",  # this shows in the parent parser
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter
                                   )
    common.add_ansible_arguments(parser)
    common.add_apt_arguments(parser)
    parser.set_defaults(func=parse_args)
