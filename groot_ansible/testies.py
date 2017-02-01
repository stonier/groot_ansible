#
# License: BSD
#    https://raw.githubusercontent.com/stonier/groot_ansible/devel/LICENSE
#
##############################################################################
# Documentation
##############################################################################

"""
Subcommand for experimental testies
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
    Launches the playbooks for bootstrapping my workstations (pc/laptop).
    """
    console.banner("'testies'")
    connection = "-c local"
    list_tasks = "--list-tasks" if args.list_tasks else ""
    # rosdistro = args.rosdistro if args.rosdistro else ros.guess_rosdistro()
    # variable_ros_release = "-e ros_release={0}".format(rosdistro) if rosdistro else ""
    variable_ros_release = ""
    # use -K before the -i if you need sudo
    cmd = "ansible-playbook testies.yaml -i localhost, {connection} {list_tasks} {variable_ros_release}".format(**locals())
    cmd = common.append_verbosity_argument(cmd, args.verbose)
    console.key_value_pairs("Ansible", {"Command": cmd}, 10)
    print("")
    subprocess.call(cmd, cwd=args.home, shell=True)


def add_subparser(subparsers):
    """
    Add our own argparser to the parent.

    :param subparsers: the subparsers factory from the parent argparser.
    """
    parser = subparsers.add_parser("testies",
                                   description="Experimental testies.",  # this shows in the help for this command
                                   help="trigger experiments",  # this shows in the parent parser
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter
                                   )
    common.add_ansible_arguments(parser)
    # ros.add_ros_arguments(parser)
    parser.set_defaults(func=parse_args)
