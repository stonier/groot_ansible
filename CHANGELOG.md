# Change Log

The format is based on [Keep a Changelog](http://keepachangelog.com/).

## [Unreleased]
### Added
- ...

### Changed
- [workstation] split between workstation and groot-workstation
- ...

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

[Unreleased]: https://github.com/stonier/groot_ansible/compare/0.2.8...HEAD
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
