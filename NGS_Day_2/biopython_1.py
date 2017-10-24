#!/usr/bin/env python3

from Bio import SeqIO

import re
import numpy

species = []
fasta = {}
descriptions = []
species_count = {}

fasta = SeqIO.parse("./uniprot_sprot.fasta", "fasta")

for seq in fasta:
	descriptions.append(seq.description)
	match = re.search('OS=([a-zA-z]+? [a-zA-Z]+?) .*', seq.description)
	if match:
		species.append(match.group(1))

for bac in species:
	if bac in species_count:
		species_count[bac] +=1
	else:
		species_count[bac] =1

print(species_count)

#	print('ID', seq_record.id)
#	print('Sequence', str(seq_record_seq))
#	print('Length', len(seq_record))
#	print('Description, seq_record.description) 




