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


from sys import platform
from os import environ, system

def write_to_rc(file_name):
    with open(file_name, 'a') as file:
        file.write('alias waffle="~/waffle/waffle/waffle.py"')
        system(f'source {file_name}')
        print("Installed waffle in PATH. Run waffle -h to confirm the success of installation")

if platform == "linux" or platform == "linux2":
    if (environ['SHELL'] == '/usr/bin/zsh'):
        linux_zsh = f"/home/{environ['USER']}/.zshrc"
        write_to_rc(linux_zsh)
    if (environ['SHELL'] == '/usr/bin/bash'):
        linux_bash = f"/home/{environ['USER']}/.bash_profile"
        write_to_rc(linux_bash)

elif platform == "darwin":
    if (environ['SHELL'] == '/bin/zsh'):
        mac_zsh = f"/Users/{environ['USER']}/.zshrc"
        write_to_rc(mac_zsh)
    if (environ['SHELL'] == '/bin/bash'):
        mac_bash = f"/Users/{environ['USER']}/.bash_profile"
        write_to_rc(mac_bash)

elif platform == "win32":
    print("Unimplemented lol")
