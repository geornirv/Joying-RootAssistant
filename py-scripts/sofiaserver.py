# -*- coding: utf-8 -*-

# sofiaserver.py - This python "helper" script deals with the several Sofiaserver.apk options

# Copyright (c) 2017 Harry van der Wolf. All rights reserved.

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public Licence as published
# by the Free Software Foundation, either version 2 of the Licence, or
# version 3 of the Licence, or (at your option) any later version. It is
# provided for educational purposes and is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public Licence for more details.

# This file is part of jrassist.


import os, platform, sys, subprocess, time
import jrfunctions

###################################################
# Variables for this script
SCRIPT_VERSION="v0.1 16 April 2017"
SCRIPT_NAME="Joying SofiaServer Mods subscript, version " + SCRIPT_VERSION

###################################################
###################################################

def init(glob_vars):
	jrfunctions.clr_scr()
	if glob_vars['MAINSCRIPT'] == "YES":
		MENU(glob_vars)
	else:
		jrfunctions.clr_scr()
		print("\n\nThis script can only be called from the main jrassist.bat or jrassist.sh script\n\n")
		jrfunctions.input_cmd("Press enter to exit\n\n")
		sys.exit()

def MENU(glob_vars):
	jrfunctions.clr_scr()
	print(87 * "=")
	print("  " + glob_vars['PROGRAM_NAME'])
	print("  " + SCRIPT_NAME)
	print(87 * "=")
	print("  Select an Option :")
	print("\n   1 . Install full NoKill/Steering Wheel mod")
	print("\n\n   2 . Install NoKill; No steering wheel mod")
	print("\n\n   3 . Install NoKill with only SRC hardcoded in")
	print("\n\n       NOTE: all versions 1, 2 and 3 include the Nav_app sound")
	print("           fix, USB output fix, Google Voice feedback fix")
	print("\n\n   4 . Update or install launcher.sh")
	print("\n\n   5 . Install extra en-US files for Google Voice")
	print("\n\n   6 . Exit this radio mods subscript")
	print(87 * "=")
	choice = jrfunctions.input_cmd("")
	### Convert string to int type ##
	choice = int(choice)
	if choice == 1:
		INSTALL_MOD(glob_vars, 'FULL')
	elif choice == 2:
		INSTALL_MOD(glob_vars, 'NoKillOnly')
	elif choice == 3:
		INSTALL_MOD(glob_vars, 'SRCOnly')
	elif choice == 4:
		INSTALL_MOD(glob_vars, 'LAUNCHER')
	elif choice == 5:
		INSTALL_MOD(glob_vars, 'extra-en-US')
	elif choice == 6:
		return
	else:
		MENU(glob_vars)


def INSTALL_MOD(glob_vars, SELECTED_MOD):
	jrfunctions.clr_scr()

