#!/usr/bin/env python3

import re

poem = open ('Python_06_nobody.txt','r')

line_count = 0

print('Start', 'End', 'Line', sep = "\t")

for line in poem:
	line_count +=1
	for match in re.finditer("Nobody", line):
		print(match.start(), match.end(), line_count, sep = "\t")

