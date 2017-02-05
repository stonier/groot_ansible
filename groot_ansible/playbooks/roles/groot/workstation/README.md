Role Name
=========

Role to handle retrieval and update of gopher software.

Requirements
------------

Ansible, apt, apt_repository.

Role Variables
--------------

* yujin_packages: list of packages to make sure are installed and up to date

All other variables are internal.

Dependencies
------------

* `yujinrobot.ros`
* `yujinrobot.public-debian-packages`

Tags
----

* `gopher-software-binaries` : binary install/upgrade
* `gopher-software-install-rosdeps` : a rosdep run after the binaries have been installed/upgraded.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    hosts:
      - localhost

    vars:
    - yujin_repository: internal
    - yujin_stream: devel

    roles:
    - role: yujinrobot.gopher-software
      gopher_software_stream: "{{ yujin_stream }}"
      gopher_software_repository: "{{ yujin_repository }}"


License
-------

Yujin

Author Information
------------------

* Daniel Stonier: stonier@yujinrobot.com
