# ===----------------- Makefile - Top-level build file --------------------===//
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

all: butter

build:
	gcc src/pancake.c -o bin/pancake

run:
	./bin/pancake

butter:
	make build && make run
