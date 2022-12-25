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

__version__ = '0.4.3'

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
            description=console.green + "A python frontend to groot playbooks." + console.reset,
            epilog=console.bold + console.white + "And his noodly appendage reached forth to tickle the blessed...\n" + console.reset,
            formatter_class=argparse.RawDescriptionHelpFormatter)
        parser.add_argument('-v', '--version', action='version', version=version_string())

        subparsers = parser.add_subparsers(title='commands',
                                           help='valid commands for groot-ansible interactions')
        update.add_subparser(subparsers)
        testies.add_subparser(subparsers)

        common.add_generic_subparser(subparsers,
                                     name="bootstrap/pc",
                                     playbook_name="bootstrap-pc",
                                     short_description="bootstrap a pc/laptop for development",
                                     description="Standard ubuntu development workstation",
                                     become_sudo=True)
        workstation.add_subparser(subparsers)

        common.add_generic_subparser(subparsers, name="os/ubuntu",
                                     playbook_name="os-ubuntu",
                                     short_description="useful non-core packages for ubuntu",
                                     description="Extra packages and configuration for the core of a basic development environment",
                                     become_sudo=True)
        common.add_generic_subparser(subparsers, name="os/kubuntu",
                                     playbook_name="os-kubuntu",
                                     short_description="kubuntu desktop packages and configuration",
                                     description="Add the kubuntu (full) desktop environment to an ubuntu installation",
                                     become_sudo=True)
        common.add_generic_subparser(subparsers, name="os/system76",
                                     playbook_name="os-system76",
                                     short_description="drivers from system76 for ubuntu",
                                     description="System76 environment setup/install/update",
                                     become_sudo=True)

        common.add_generic_subparser(subparsers, name="devel/git",
                                     playbook_name="devel-git",
                                     short_description="git binaries, modules and configuration",
                                     description="Git binaries, modules (lfs) and user configuration",
                                     become_sudo=True)
        common.add_generic_subparser(subparsers, name="devel/powerline",
                                     playbook_name="devel-powerline",
                                     short_description="powerline in the shell for the user",
                                     description="Setup powerline in the shell for the user",
                                     become_sudo=True)
        ros.add_subparser(subparsers)
        common.add_generic_subparser(subparsers, name="devel/ros2",
                                     playbook_name="devel-ros2",
                                     short_description="ros2 environment for ubuntu",
                                     description="ROS 2 environment setup/install/update",
                                     become_sudo=True)
        
        common.add_generic_subparser(subparsers, name="extras/chrome",
                                     playbook_name="extras-chrome",
                                     short_description="google chrome for ubuntu",
                                     description="Google chrome setup/install/update",
                                     become_sudo=True)
        common.add_generic_subparser(subparsers, name="extras/vscode",
                                     playbook_name="extras-vscode",
                                     short_description="vscode for ubuntu",
                                     description="VSCode setup/install/update",
                                     become_sudo=True)
        common.add_generic_subparser(subparsers, name="extras/snorriheim",
                                     playbook_name="extras-snorriheim",
                                     short_description="snorriheim ppa and packages",
                                     description="Snorriheim's PPA and packages for ubuntu",
                                     become_sudo=True)
        options = parser.parse_args(args)
        # options, unused_unknown_args = parser.parse_known_args(args)
        options.func(options)  # relay arg parsing to the subparser configured `set_defaults` function callback

    except KeyboardInterrupt:
        print('Interrupted by user!')
