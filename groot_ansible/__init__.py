#
# License: BSD
#    https://raw.githubusercontent.com/stonier/groot_ansible/devel/LICENSE
#
##############################################################################
# Documentation
##############################################################################

"""
Python wrapped ansible scripts for installing and updating systems for
various use cases.
"""

##############################################################################
# Imports
##############################################################################

import argparse

from . import common
from . import console
from . import ros
from . import update
from . import testies
from . import workstation

##############################################################################
# Constants
##############################################################################

__version__ = '0.2.14'

##############################################################################
# Main
##############################################################################


def version_string():
    return console.cyan + "Version" + console.reset + " : " + console.yellow + __version__ + console.reset


def main(args=None):
    """
    Entry point to the console 'groot-ansible' tool.
    """
    try:
        parser = argparse.ArgumentParser(
            description="A frontend to groot playbooks.",
            epilog="And his noodly appendage reached forth to tickle the blessed...\n",
            formatter_class=argparse.RawDescriptionHelpFormatter)
        parser.add_argument('-v', '--version', action='version', version=version_string())
        subparsers = parser.add_subparsers(title='commands',
                                           help='valid commands for groot-ansible interactions')
        update.add_subparser(subparsers)
        ros.add_subparser(subparsers)
        workstation.add_subparser(subparsers)
        common.add_generic_subparser(subparsers, "ubuntu",
                                     short_description="extras for a development environment",
                                     description="Extra packages and configuration for the core of a basic development environment",
                                     become_sudo=True)
        common.add_generic_subparser(subparsers, "kubuntu",
                                     short_description="switch to a kubuntu (full) environment",
                                     description="Add the kubuntu (full) desktop environment to an ubuntu installation",
                                     become_sudo=True)
        common.add_generic_subparser(subparsers, "git",
                                     short_description="git binaries, modules and configuration",
                                     description="Git binaries, modules (lfs) and user configuration",
                                     become_sudo=True)
        common.add_generic_subparser(subparsers, "chrome",
                                     short_description="google chrome for ubuntu",
                                     description="Google chrome setup/install/update",
                                     become_sudo=True)
        common.add_generic_subparser(subparsers, "drive",
                                     short_description="google drive for ubuntu",
                                     description="Google drive setup/install/update",
                                     become_sudo=True)
        common.add_generic_subparser(subparsers, "powerline",
                                     short_description="powerline in the shell for the user",
                                     description="Setup powerline in the shell for the user",
                                     become_sudo=True)
        common.add_generic_subparser(subparsers, "gazebo",
                                     short_description="gazebo and related packages for ubuntu",
                                     description="Gazebo repository setup/install/update",
                                     become_sudo=True)
        common.add_generic_subparser(subparsers, "ros2",
                                     short_description="ros2 environment for ubuntu",
                                     description="ROS 2 environment setup/install/update",
                                     become_sudo=True)
        common.add_generic_subparser(subparsers, "workstation",
                                     short_description="standard development environment for ubuntu",
                                     description="Standard setup/install/update for a development workstation",
                                     become_sudo=True)
        testies.add_subparser(subparsers)
        options = parser.parse_args(args)
        # options, unused_unknown_args = parser.parse_known_args(args)
        options.func(options)  # relay arg parsing to the subparser configured `set_defaults` function callback

    except KeyboardInterrupt:
        print('Interrupted by user!')
