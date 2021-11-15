#!/usr/bin/env python3

# ===----------------- installer.py - File for installing waffle ------------===//
#
# This source file is part of the waffle open source project
#
# Copyright (c) 2021 KittyBorgX and the waffle project authors
# Licensed under Apache License v2.0 with Runtime Library Exception
#
# See https://github.com/KittyBorgX/waffle/blob/main/LICENSE for license information
# See https://github.com/KittyBorgX/waffle/blob/main/CONTRIBUTORS.md for the list of waffle project contributors
#
# ===----------------------------------------------------------------------===//


from posixpath import expanduser
from sys import platform
from os import environ, path, stat, system
from pathlib import Path

# error free?
shell = environ.get('SHELL', '')

def check_file_existance(file_name):
    if not path.exists(file_name) or stat(file_name).st_size == 0:
        open(file_name, 'w')

def write_to_rc(file_name):
    check_file_existance(file_name)

    # check if installer has already ran, warn
    for line in open(file_name, 'r').readlines():
        if 'alias waffle' in line:
            print('Waffle alias found in your configuration file, not finishing instalation.')
            exit()

    open(file_name, 'a').write(f'alias waffle=\'{Path(__file__).parent.resolve()}/waffle/waffle.py\'')

    print('Successfully made waffle globally acessible, reloading shell for changes to take effect...')

    # auto reload shell
    system(shell)

if platform in ['linux', 'linux2', 'darwin']:    
    if not shell:
        print('The SHELL environmental variable is missing.')
        exit()

    # to be appended to later on
    conf_file = expanduser('~/');

    if shell in ['/bin/zsh', '/usr/bin/zsh']:
        conf_file += '.zshrc'

    if shell in ['/bin/bash', '/usr/bin/bash']:
        if platform == 'darwin':
            conf_file += '.bash_profile'
        
        else:
            conf_file += '.bash_aliases'
    
    write_to_rc(conf_file)

elif platform == "win32":
    print("Unimplemented lol")
