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
module: vci
short_description: Find and import vcs repos from an index
'''

EXAMPLES = '''
- name: Find and import a vcs workspace
  vci:
    key: catkin
    path: /tmp/foo

- name: Find, import or update (if exists) a vcs workspace
  vci:
    key: catkin
    path: /tmp/foo
    force: true

- name: Find, import from a specified index
  vci:
    key: catkin
    index: https://raw.githubusercontent.com/stonier/vci/repos/kinetic.yaml
    path: /tmp/foo
'''

##############################################################################
# Implementation
##############################################################################


def main():
    module = ansible.module_utils.basic.AnsibleModule(
        argument_spec  = dict(                                                        #@IgnorePep8
            key        = dict(required=True, type='str'),                             #@IgnorePep8
            index      = dict(default='',    type='str'),                             #@IgnorePep8
            path       = dict(default='.',   type='str'),                             #@IgnorePep8
            force      = dict(default=False, type='bool'),                            #@IgnorePep8
            # pull      = dict(default=True, type='bool'),                            #@IgnorePep8
        )
    )
    abs_path = os.path.abspath(module.params["path"])
    if os.path.exists(abs_path):
        if not module.params["force"]:
            module.exit_json(changed=False,
                             msg="already exists and 'force' is not requested",
                             index=module.params["index"],
                             yaml="",
                             output="",
                             parameters=module.params)
    else:
        os.makedirs(abs_path)

    if not module.params["index"]:
        try:
            cmd = "vci config --no-colour"
            index = subprocess.check_output(cmd, shell=True)
        except subprocess.CalledProcessError as e:
            module.fail_json(msg="Failed to retrieve current index [{0}]".format(str(e)),
                             cmd=cmd,
                             index=module.params['index'],
                             yaml="",
                             output=e.output,
                             parameters=module.params
                             )
            return
    else:
        index = module.params['index']

    try:
        cmd = "vci find --index={index} {key}".format(index=index, key=module.params["key"])
        yaml = subprocess.check_output(cmd, cwd=abs_path, shell=True)
    except subprocess.CalledProcessError as e:
        module.fail_json(msg="Failed to find key '{0}'".format(module.params['key']),
                         cmd=cmd,
                         index=index,
                         yaml="",
                         output=e.output,
                         parameters=module.params)
        return

    cmd = "vci find --index={index} {key} | vcs import".format(index=index, key=module.params["key"])

    changed = False
    try:
        out = subprocess.check_output(cmd, cwd=abs_path, shell=True)
        if any(keyword in out for keyword in ['Cloning', 'behind']):
            changed = True
    except subprocess.CalledProcessError as e:
        module.fail_json(msg="Failed to import key '{0}'".format(module.params['key']),
                         cmd=cmd,
                         index=index,
                         yaml=yaml,
                         output=e.output,
                         parameters=module.params)
        return
    else:
        module.exit_json(changed=changed,
                         index=index,
                         yaml=yaml,
                         output=out,
                         parameters=module.params)
    # TODO : implement a pull


if __name__ == '__main__':
    main()
