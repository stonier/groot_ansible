#!/usr/bin/python

##############################################################################
# Library
##############################################################################

import ansible.module_utils.basic
import datetime
import json
import sys

##############################################################################
# Library
##############################################################################


def main():

#     module = ansible.module_utils.basic.AnsibleModule(argument_spec={})
#     response = {"hello": "world"}
#     module.exit_json(changed=False, meta=response)
    date = str(datetime.datetime.now())
    print json.dumps({
        "time" : date
    })
    sys.exit(0)

if __name__ == '__main__':
    main()
