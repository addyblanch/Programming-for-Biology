#!/usr/bin/env python3

import re

apoi = open("Python_06_ApoI.fasta", "r")

#creates two dictionaries one with original data and second with reverse complemenet data
genes = {}
seq_d = {}
seq_d_cut = ''

#assign key and value for the dictionaries
id = ""
seq = ""

#for loop to create first dictionary by taking fasta header to the key and each line of the sequence and joining them together into a single line
for line in apoi:
	if '>' in line:
		id = (line.strip())	
		genes[id]=seq	
	else:
		seq = (line.strip())
		genes[id]+=seq

for id,seq_d in genes.items():
	recog = re.findall(r"([AG]AATT[CT])", seq_d)
	print(recog)

	seq_d_cut = re.sub(r'([AG])(AAT[CT])', r'\1^\2', seq_d)
	print(seq_d_cut)

	restrict_cut = seq_d_cut.split('^')
	restrict_sort = sorted(restrict_cut, key=len, reverse=True)
print(restrict_sort)

	
