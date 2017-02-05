# Groot Ansible

## Usage

First time usage:

```
# Download the bootstrap script
wget https://raw.githubusercontent.com/stonier/groot_ansible/devel/scripts/groot-ansible-bootstrap
chmod 755 groot-ansible-bootstrap
./groot-ansible-bootstrap
```

Regular usage:

```bash
# Update the groot ansible environment
$ groot-ansible update
# Check the list of subcommands (ansible playbooks) you can run
$ groot-ansible --help
usage: groot-ansible [-h] [-v]
                     {update,ros,workstation,ubuntu,kubuntu,git,chrome,drive,powerline,testies}
                     ...

A frontend to groot playbooks

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show the version number and exit

commands:
  {update,ros,workstation,ubuntu,kubuntu,git,chrome,drive,powerline,testies}
                        valid commands for groot-ansible interactions
    update              update your ansible/apt environment
    ros                 ros distro on an ubuntu machine
    workstation         bootstrap a pc/laptop for development
    ubuntu              extras for a development environment
    kubuntu             switch to a kubuntu (full) environment
    git                 git binaries, modules and configuration
    chrome              google chrome for ubuntu
    drive               google drive for ubuntu
    powerline           powerline in the shell for the user
    testies             trigger experiments

And his noodly appendage reached forth to tickle the blessed...
# Example : setup the google drive utility from ppa
$ groot-ansible drive
```

## Dev Notes

Some rough guidelines (in much need of explanation).

* Avoid tags in roles, it adds complexity (see also [here](https://www.theodo.fr/blog/2015/10/best-practices-to-build-great-ansible-playbooks/))
* Roles as minimal, fundamental jobs that can be composed by playbooks
* ...

## Tags, Playbooks, Roles

The following three entities can be used in a variety of ways - e.g. roles and playbooks
both can be used to help share procedures and it is easy to get mixed up about
what to use and what not. Some conventions that I am currently sticking to.

* **Tags** : for dev handles that enable 'mucking around' with what is getting done.
* **Roles** : use as much as possible to share jobs
* **Playbooks** : to script use cases

