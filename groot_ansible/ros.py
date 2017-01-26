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
import platform
import subprocess

from . import common
from . import console

##############################################################################
# Methods
##############################################################################


def add_ros_arguments(parser):
    """
    Arguments relevant for a ros system.

    :param argparse.ArgumentParser parser:
    """
    group = parser.add_argument_group(title="ros arguments")
    group.add_argument('--rosdistro', action='store', default=None, help='manually specify the ros release to install/update')
#     group.add_argument('--only-upgrade', action='store_true', help='only upgrade currently installed ros debians')
#     group.add_argument('--only-rosdeps', action='store_true', help='only do the --install-rosdeps step')
#     group.add_argument('--skip-rosdeps', action='store_true', help='skip the --install-rosdeps step')


def guess_rosdistro():
    distro_map = {'trusty': 'indigo', 'xenial': 'kinetic'}
    unused_os, unused_version, codename = platform.linux_distribution()
    return distro_map[codename] if codename in distro_map.keys() else None  # let the role decide the default if we don't guess it


def parse_args(args):
    """
    Launches the playbooks for managing the ros software environment on a pc.
    """
    console.banner("'ros'")
    connection = "-c local"
    list_tasks = "--list-tasks" if args.list_tasks else ""
    # TODO check for a valid rosdistro on this platform
    rosdistro = args.rosdistro if args.rosdistro else guess_rosdistro()
    variable_ros_release = "-e ros_release={0}".format(rosdistro) if rosdistro else ""
    cmd = "ansible-playbook ros.yaml -K -i localhost, {connection} {list_tasks} {variable_ros_release}".format(**locals())
    cmd = common.append_verbosity_argument(cmd, args.verbose)
    console.key_value_pairs("Parameters", {"Rosdistro": rosdistro}, 10)
    console.key_value_pairs("Ansible", {"Command": cmd}, 10)
    print("")
    subprocess.call(cmd, cwd=args.home, shell=True)


def add_subparser(subparsers):
    """
    Add our own argparser to the parent.

    :param subparsers: the subparsers factory from the parent argparser.
    """
    parser = subparsers.add_parser("ros",
                                   description="Install, configure or update an existing ros distro.",  # this shows in the help for this command
                                   help="ros distro on an ubuntu machine",  # this shows in the parent parser
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter
                                   )
    common.add_ansible_arguments(parser)
    add_ros_arguments(parser)
    parser.set_defaults(func=parse_args)
