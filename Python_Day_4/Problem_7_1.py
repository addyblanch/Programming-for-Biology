#!/usr/bin/env python3

import sys
import re

dna = open(sys.argv[1], 'r')
seq_len = int(sys.argv[2])
fmt_fasta = open(sys.argv[3], 'w')


def format_dna(sequence, seq_len):
	new_seq = ''
	sequence = re.sub('\n', '', sequence)
	sequence = sequence.strip()
	
	while sequence:
		if len(sequence) >= seq_len:
			new_seq += sequence[0:seq_len] + '\n'
			sequence = sequence[seq_len:len(sequence)]
		else:
			new_seq += sequence[0:len(sequence)]
			sequence = ''
	return new_seq

nuc = ''

for line in dna:
	if '>' in line:
		nuc = line.strip()
		fmt_fasta.write(nuc + '\n')
	else:
		nuc = line.strip()
		nuc += nuc
		new_out = format_dna(nuc, seq_len)
		fmt_fasta.write(new_out + '\n')
