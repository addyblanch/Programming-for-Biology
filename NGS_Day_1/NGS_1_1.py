#!/usr/bin/env python3

import sys
import re
import numpy

fastq = open(sys.argv[1], 'r')

seq_count = 0
line_num = 0
seq_length = []
seq_qual = []
total_qual = []

for line in fastq:
	line_num +=1
	line = line.strip()
	if line_num %4 == 1:
		seq_count += 1
	
	elif line_num %4 == 2:
		seq_length.append(len(line))

	elif line_num %3 == 3:
		continue

	elif line_num %4 == 0:	
		for qual in line:
			seq_qual.append(ord(qual) -33)
		total_qual.append(numpy.average(seq_qual))

	
avg_length = numpy.average(len(line))
len_std = numpy.std(len(line))
avg_qual = numpy.average(seq_qual)
qual_std = numpy.std(seq_qual)

print("There are", seq_count, "sequences", "with an average length of",  avg_length, "bp and a length standard deviation of", len_std, "\n", "The mean quality of the sequence reads is", avg_qual, "and the standard deviation of the quaultiy is", qual_std)
