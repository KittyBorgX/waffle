#!/usr/bin/env python3

from sys import platform
from os import environ, system


def write_to_rc(file_name):
    with open(file_name, 'a') as file:
        file.write('alias waffle="~/waffle/waffle/waffle.py"')
        system(f'source {file_name}')
        print("Installed waffle in PATH. Run waffle -h to confirm the success of installation")


if platform == "linux" or platform == "linux2":
    # linux
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
    # Windows...
