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

from . import console
from . import ros
from . import update
from . import workstation

##############################################################################
# Constants
##############################################################################

__version__ = '0.2.2'

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
            description="version control index handling",
            epilog="And his noodly appendage reached forth to tickle the blessed...\n",
            formatter_class=argparse.RawDescriptionHelpFormatter)
        parser.add_argument('-v', '--version', action='version', version=version_string())
        subparsers = parser.add_subparsers(title='commands',
                                           help='valid commands for groot-ansible interactions')
        update.add_subparser(subparsers)
        ros.add_subparser(subparsers)
        workstation.add_subparser(subparsers)
        options = parser.parse_args(args)
        # options, unused_unknown_args = parser.parse_known_args(args)
        options.func(options)  # relay arg parsing to the subparser configured `set_defaults` function callback

    except KeyboardInterrupt:
        print('Interrupted by user!')
