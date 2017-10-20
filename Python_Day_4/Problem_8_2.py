#!/usr/bin/env python3

import sys
import re

class NotValidSeq(Exception):
	pass

try:
	file = sys.argv[1]
	print("Fasta provided:", file)
	
	if not file.endswith('.fa') or not file.endswith('fasta') or not files.endswith('.nt'):
		raise ValueError("Not a valid file format") 	

	dna = open(file, 'r')

	codon_frame = open(Codon_frame1.txt, "w")

	genes = {}

	#assign key and value for the dictionaries	
	id = ""
	seq = ""

	#for loop to create first dictionary by taking fasta header to the key and each line of the sequence and joining them together into a $
	for line in dna:
		if '>' in line:
			id = (line.strip())
			genes[id]=seq
		else:
			seq = (line.strip())
			genes[id]+=seq
			if re.search('[^ATGCN]+',genes[id]):
				raise NotValidSeq("Not nucleotide characters")

	#Count occurance of each nucleotide
	for seq in genes:
		codons = re.findall(r"(.{3})", genes[seq])
		genes[seq] = codons
	
		for codon in codons:
			codon_frame.write(seq+"\n"+codon+"\n")

except IndexError:
	print("No File Provided")
except IOError:
	print("Cannot find file", file, ':', ex.sterror)
except ValueError:
	print("Not a valid file format")
except NotValidSeq:
	print("Invalid nucleotide characters in file")
