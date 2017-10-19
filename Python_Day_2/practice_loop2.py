#!/usr/bin/env python3

import sys

#Script to create a print a range tkaing range from command line

a = int(sys.argv[1])
b = int(sys.argv[2])

for num in range(a,b):
	if num%2 != 0:
		print(num)
