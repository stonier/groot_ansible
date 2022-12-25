# Change Log

The format is based on [Keep a Changelog](http://keepachangelog.com/).

## [Unreleased]
### Added
* ...

### Changed
* ...

## [0.4.3] - 2022-12-25
### Added
* [ubuntu] added default-jdk as a core system dependency
* [extras/vscode] replacing eclipse as the installed ide

### Changed
* [groot/workstation] option to force vci

### Removed
* [groot/workstation] eclipse replaced by vscode
* [groot/workstation] drive no longer used

## [0.4.2] - 2020-12-30
### Changed
- [infra] fix local deb build and instructions in README
- [workstation] added gist.github.com to .netrc

## [0.4.1] - 2020-07-11
### Added
- [bootstrap/daniel] added .xprofile language configuration
- [snorriheim] python-groot-tools->python3-groot-tools

### Changed
- [infra] dependencies for building debs directly

## [0.4.0] - 2020-06-25
### Changed
- [focal] upgraded to support ubuntu focal (20.04)

## [0.3.5] - 2019-09-16
### Added
- [ros2] rosdep install, init and update

## [0.3.4] - 2019-09-16
### Added
- [ubuntu] net-tools, python3-pip, python3-stdeb

### Changed
- [snorriheim] python-vci -> python3-vci
- [bootstrap/daniel] add ros2, remove unneeded comment for ros-snorriheim
- [bootstrap/daniel] move ros2 prior to workspace installs (needs vcs)
- [bootstrap/daniel] drop ros1
- [ubuntu] bugfix typo [stdep->stdeb]

## [0.3.0] - 2018-12-28
### Added
- [ros2] role for installation/maintenance of ROS2
- [infra] docker now bootstrapped as a system group (docker.io fails otherwise)

### Changed
- [all] overhauled with support for Ubuntu Bionic (18.04)
- [frontends] more modular to enable testing of smaller groups
- [frontends] bootstrap playbooks for one-shot everything style playbooks

## [0.2.14] - 2017-03-17
### Changed
- [groot/workstation] bash aliases for vci
- [powerline] switch to gitstatus

## [0.2.13] - 2017-03-16
### Changed
- [groot/workstation] ensure workspaces path exists
- [chrome] match apt url exactly as a workaround for the mystery google-chrome.list

## [0.2.12] - 2017-03-15
### Added
- [groot/workstation] kde-config-fcitx for kde configuration of the input method

### Changed
- [groot/workstation] .pypirc password in the vault

## [0.2.11] - 2017-03-15
### Added
- [groot/workstation] fcitx, fcitx-hangul dependencies added for input methods

### Changed
- [kubuntu] bugfix missing comma in anti-kubuntu package list
- [groot/workstation] alias for cdw

## [0.2.10] - 2017-02-12
### Added
- [groot/workstation] creating and importing my public/private keys

### Changed
- [groot/workstation] .netrc configured via a vault variable now

## [0.2.9] - 2017-02-10
### Added
- [groot/workstation] ttygif
- [ubuntu] ttyrec
- [kubuntu] usb-creator-kde

### Changed
- [workstation] split between workstation and groot-workstation

## [0.2.8] - 2017-02-06
### Added
- [ros2] role, subcommand added
- [gazebo] role, subcommand added

### Changed
- [groot/workstation] vcs_extras -> vci
- [workstation] split between workstation and groot-workstation

## [0.2.7] - 2017-02-06
### Changed
- [vci] bugfix non-use of the index variable
- [bootstrap] comment reminding to login in case of group changes
- [workstation] bugfix non-creation of ~/.config/fcitx

## [0.2.6] - 2017-02-05
### Changed
- [workstation] role renamed to groot/workstation
- [workstation] help for the drive Makefile

## [0.2.5] - 2017-02-04
### Added
- [workstation] python .pypirc configuration template added

## [0.2.4] - 2017-02-04
### Changed
- [workstation] google drive helper Makefile
- [workstation] eclipse startup script for groot-eclipse

## [0.2.3] - 2017-02-02
### Added
- [vci] module added
- [testies] role, playbook, subcommand added
- [chrome] role, playbook, subcommand added
- [drive] role, playbook, subcommand added
- [git] role, playbook, subcommand added
- [ubuntu] role, playbook, subcommand added
- [kubuntu] role, playbook, subcommand added
- [powerline] role, playbook, subcommand added

### Changed
- [workstation] complete functionality of first iteration

## [0.2.2] - 2017-01-29
### Added
- [workstation] enable canonical partner repositories
- [workstation] create ~/.gnupg directory
- [workstation] purge unity conflict packages before installing kubuntu-full
- [workstation] gitconfig setup
- [workstation] netrc setup

### Changed
- [workstation] role tasks modularised

## [0.2.1] - 2017-01-26
### Changed
- [infra] bugfix install rule trying to install roles dir

## [0.2.0] - 2017-01-26
### Added
- [bootstrap] user groups
- [bootstrap] ansible/snorriheim ppas
- [ros] generic ros install/update
- [workstation] lots of ppa's and debs
- [update] updates itself and ansible

## [0.1.0] - 2017-01-26
### Added
- [infra] skeleton structure

[Unreleased]: https://github.com/stonier/groot_ansible/compare/0.3.5...HEAD
[0.3.5]: https://github.com/stonier/groot_ansible/compare/0.3.4...0.3.5
[0.3.4]: https://github.com/stonier/groot_ansible/compare/0.2.14...0.3.4
[0.2.14]: https://github.com/stonier/groot_ansible/compare/0.2.13...0.2.14
[0.2.13]: https://github.com/stonier/groot_ansible/compare/0.2.12...0.2.13
[0.2.12]: https://github.com/stonier/groot_ansible/compare/0.2.11...0.2.12
[0.2.11]: https://github.com/stonier/groot_ansible/compare/0.2.10...0.2.11
[0.2.10]: https://github.com/stonier/groot_ansible/compare/0.2.9...0.2.10
[0.2.9]: https://github.com/stonier/groot_ansible/compare/0.2.8...0.2.9
[0.2.8]: https://github.com/stonier/groot_ansible/compare/0.2.7...0.2.8
[0.2.7]: https://github.com/stonier/groot_ansible/compare/0.2.6...0.2.7
[0.2.6]: https://github.com/stonier/groot_ansible/compare/0.2.5...0.2.6
[0.2.5]: https://github.com/stonier/groot_ansible/compare/0.2.4...0.2.5
[0.2.4]: https://github.com/stonier/groot_ansible/compare/0.2.3...0.2.4
[0.2.3]: https://github.com/stonier/groot_ansible/compare/0.2.2...0.2.3
[0.2.2]: https://github.com/stonier/groot_ansible/compare/0.2.1...0.2.2
[0.2.1]: https://github.com/stonier/groot_ansible/compare/0.2.0...0.2.1
[0.2.0]: https://github.com/stonier/groot_ansible/compare/0.1.0...0.2.0
[0.1.0]: https://github.com/stonier/groot_ansible/compare/d85f7d176f25cf9bec221bd309cd3e4c942891ad...0.1.0
