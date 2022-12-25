#!/usr/bin/python

##############################################################################
# Library
##############################################################################

# from ansible.module_utils.basic import * #@IgnorePep8

import ansible.module_utils.basic
import os
import subprocess

##############################################################################
# Documentation
##############################################################################

DOCUMENTATION = '''
---
module: vci_config
short_description: Configure a vci index url
'''

EXAMPLES = '''
- name: Configure uri with a url (do not override unless force is true)
  vci_config:
    index: https://raw.githubusercontent.com/stonier/vci/repos/kinetic.yaml
    force: true
'''

##############################################################################
# Implementation
##############################################################################


def main():
    module = ansible.module_utils.basic.AnsibleModule(
        argument_spec  = dict(                                                        #@IgnorePep8
            index      = dict(required=True, type='str'),                             #@IgnorePep8
            force      = dict(default=False, type='bool'),                            #@IgnorePep8
        )
    )
    try:
        cmd = "vci config --no-colour"
        index = subprocess.check_output(cmd, shell=True).rstrip()
        vci_configured = True
        print(f"VCI Configured: {index}")
    except subprocess.CalledProcessError as e:
        index = None
        vci_configured = False
        print(f"VCI Not Configured")

    print(f"Configure with {module.params['index']}")
    if not module.params["force"] and vci_configured:
        module.exit_json(msg="VCI already configured, refusing to override as requested",
                         changed=False,
                         index=index,
                         parameters=module.params)

    if index and (module.params['index'] == index):
        module.exit_json(msg="VCI already configured with the specified index",
                         changed=False,
                         index=index,
                         parameters=module.params)

    index = module.params['index']

    try:
        cmd = "vci config --no-colour {index}".format(index=index)
        yaml = subprocess.check_output(cmd, shell=True)
    except subprocess.CalledProcessError as e:
        module.fail_json(msg="Failed to configure the index '{}'".format(index),
                         cmd=cmd,
                         index=index,
                         yaml="",
                         output=e.output,
                         parameters=module.params)
        return

    module.exit_json(changed=True,
                        index=index,
                        yaml=yaml,
                        parameters=module.params)

if __name__ == '__main__':
    main()
