#!/usr/bin/env python3

import sys
import re
import numpy

fastq = open(sys.argv[1], 'r')

seq_count = 0
seq_qual = []
trim_site = 0

for line in fastq:
	if line_num %4 == 0:
		for qt in line:
			seq_qual.append(ord(qual) -33)


	elif line_num % == 2
		for nt in line:
			



