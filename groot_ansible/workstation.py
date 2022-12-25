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
# from . import ros


##############################################################################
# Methods
##############################################################################


def parse_args(args):
    """
    Launches the playbooks for bootstrapping my workstations (pc/laptop).
    """
    console.banner("'groot-workstation'")
    connection = "-c local"
    list_tasks = "--list-tasks" if args.list_tasks else ""
    # rosdistro = args.rosdistro if args.rosdistro else ros.guess_rosdistro()
    # variable_ros_release = "-e ros_release={0}".format(rosdistro) if rosdistro else ""
    variable_ros_release = ""
    force = "-e vci_force_index=true" if args.vci_force_index else "-e vci_force_index=false"
    cmd = "ansible-playbook bootstrap-daniel.yaml --ask-vault-pass -K -i localhost, {connection} {list_tasks} {variable_ros_release} {force}".format(**locals())
    cmd = common.append_verbosity_argument(cmd, args.verbose)
    console.key_value_pairs("Ansible", {"Command": cmd}, 10)
    print("")
    subprocess.call(cmd, cwd=args.home, shell=True)


def add_subparser(subparsers):
    """
    Add our own argparser to the parent.

    :param subparsers: the subparsers factory from the parent argparser.
    """
    parser = subparsers.add_parser("bootstrap/daniel",
                                   description="Daniel's customised kubuntu development workstation",  # this shows in the help for this command
                                   help="bootstrap a pc/laptop for development (Daniel)",  # this shows in the parent parser
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter
                                   )
    common.add_ansible_arguments(parser)
    group = parser.add_argument_group(title="workstation arguments")
    group.add_argument('-f', '--vci-force-index', action='store_true', help='override vci configuration')
    # ros.add_ros_arguments(parser)
    parser.set_defaults(func=parse_args)
