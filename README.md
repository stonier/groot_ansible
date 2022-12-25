# Groot Ansible

## Usage - With Debs


```
# 1) Download the bootstrap script
$ wget https://raw.githubusercontent.com/stonier/groot_ansible/devel/scripts/groot-ansible-bootstrap
$ chmod 755 groot-ansible-bootstrap
$ ./groot-ansible-bootstrap

# 2) Install
$ groot-ansible --help
$ groot-ansbile extras/chrome       (not strictly necessary, but good to test)
$ groot-ansible bootstrap/daniel -f (force vci to configure the index)

# 3) Update
$ groot-ansible utils/update  # update itself
```

## Usage - From Sources

If I don't have the deb built yet, then it will fail to fetch `python-groot-ansible` and you'll need to clone the repo and source the setup script which will fetch any dependencies it requires and boot you into a virtual environment.

```
# 1) Get Groot Ansible
$ sudo apt install git
$ git clone https://github.com/stonier/groot_ansible

# 2) Drop into a Venv
$ cd groot_ansible
$ . ./venv.bash

# 3) First time Setup (ignore the deb fail if no debs exist)
$ cd scripts
$ ./groot-ansible-bootstrap

# 4) Relogin/reboot (if groups changed)

# 5) Manual Preparation (not yet automated)
#    Generate and add an ssh key to github

# 6) Start Installing!
$ groot-ansbile extras/chrome       (not strictly necessary, but good to test)
$ groot-ansible bootstrap/daniel -f (force vci to configure the index)
```

## Usage - Help

```bash
$ groot-ansible --help
usage: groot-ansible [-h] [-v]
                     {utils/update,utils/testies,bootstrap/pc,bootstrap/daniel,os/ubuntu,os/kubuntu,os/system76,devel/git,devel/powerline,devel/ros1,devel/ros2,extras/chrome,extras/snorriheim,extras/vscode}
                     ...

A frontend to groot playbooks

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show the version number and exit

commands:
  {utils/update,utils/testies,bootstrap/pc,bootstrap/daniel,os/ubuntu,os/kubuntu,os/system76,devel/git,devel/powerline,devel/ros1,devel/ros2,extras/chrome,extras/snorriheim}
                        valid commands for groot-ansible interactions
    utils/update        update your ansible/apt environment
    utils/testies       trigger experiments
    bootstrap/pc        bootstrap a pc/laptop for development
    bootstrap/daniel    bootstrap a pc/laptop for development (Daniel)
    os/ubuntu           useful non-core packages for ubuntu
    os/kubuntu          kubuntu desktop packages and configuration
    os/system76         drivers from system76 for ubuntu
    devel/git           git binaries, modules and configuration
    devel/powerline     powerline in the shell for the user
    devel/ros1          ros1 environment for ubuntu
    devel/ros2          ros2 environment for ubuntu
    extras/chrome       google chrome for ubuntu
    extras/snorriheim   snorriheim ppa and packages
    extras/vscode       vscode for ubuntu

And his noodly appendage reached forth to tickle the blessed...

$ groot-ansible extras/chrome
$ groot-ansible extras/vscode
```

## Dev Notes

Some rough guidelines (in much need of explanation).

* Avoid tags in roles, it adds complexity (see also [here](https://www.theodo.fr/blog/2015/10/best-practices-to-build-great-ansible-playbooks/))
* Roles as minimal, fundamental jobs that can be composed by playbooks
* ...

### Tags, Playbooks, Roles

The following three entities can be used in a variety of ways - e.g. roles and playbooks
both can be used to help share procedures and it is easy to get mixed up about
what to use and what not. Some conventions that I am currently sticking to.

* **Tags** : for dev handles that enable 'mucking around' with what is getting done.
* **Roles** : use as much as possible to share jobs
* **Playbooks** : to script use cases

### Debs

```
make deb
cd deb_dist
sudo dpkg -i python3-groot-ansible-<tab><tab>
```
