#!/usr/bin/env python3

import sys
import re


dna = open(sys.argv[1], "r")

genes = {}

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

#Count occurance of each nucleotide
for seq in genes:
	A_count = genes[seq].count('A')
	T_count = genes[seq].count('T')
	G_count = genes[seq].count('G')
	C_count = genes[seq].count('C')

#creating another set of key values to match each nucleotide
	genes[seq] = {"A" : A_count, "T" : T_count, "G" : G_count, "C" : C_count}

#print out the sequnce id along with teh ATCG content
	print ("Sequence", seq, "A content is" , A_count, "T content is", T_count,  "G content is", G_count, "C content is", C_count)

