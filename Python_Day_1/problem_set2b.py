#!/usr/bin/env python3

#Script to test if statement is true but pulling from commandline

import sys

statement = float(sys.argv[1])

if statement == 34:
	print('This is true')

else:
	print('This is not true')
