# TaskWarrior hooks

This repository contains TaskWarrior hooks I'm using.

## Hooks list

| Hook name | Description | Dependencies |
| --------- | ----------- | ------------ |
| due-eod | Sets 'due' field to end of day, replacing default "00:00:00" with "23:59:59". | Python 3.7+ |

## Installing

Clone repository somewhere and create symlinks to hooks directory. Usually it is `${HOME}/.task/hooks`. Create this directory if not present.

See hooks list above for dependencies needed.

There are no makefile or other installation scripts intentionally, **you have to read [this document](https://taskwarrior.org/docs/hooks.html) and understand it!**

## Reporting bugs

Please go to [my gitea](https://code.pztrn.name/misc/taskwarrior_hooks) for bug reporting. All other places are mirrors.
