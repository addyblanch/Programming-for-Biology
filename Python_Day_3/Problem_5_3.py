#!/usr/bin/env python3

import sys

#opens file from command line in read only mode

dna = open(sys.argv[1], "r")
output = open(sys.argv[2], "w")

#creates two dictionaries one with original data and second with reverse complemenet data
genes = {}
genes_comp = {}

#assign key and value for the dictionaries
id = ""
seq = ""

#for loop to create first dictionary by taking fasta header to the key and each line of the sequence and joining them together into a single line
for line in dna:
	if '>' in line:
		id = (line.strip())	
		genes[id]=seq	
	else:
		seq = (line.strip())
		genes[id]+=seq

#calling each key and altering the value to a reverse complement of the sequence
for line in genes:
	seq_comp = (genes[line].replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c'))

	seq_comp_upper = seq_comp.upper()

	seq_rev_comp = seq_comp_upper[::-1]

	genes_comp[line]=seq_rev_comp

#print second dictionary to output file

for line in genes_comp:
	output.write(line+"\n"+genes_comp[line]+"\n")
