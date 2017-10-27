#!/usr/bin/env python3

import sys, os, re

sam = open(sys.argv[1], 'r')

gene_dict = {}

for line in sam:
	line = line.rstrip()
	fields = line.split('\t')

	read_name = fields[0]
	combo_name = fields[2]	
	
	(gene_id, transcript_id) = combo_name.split("^")

	if gene_id not in gene_dict:
		gene_dict[gene_id] = set()

	gene_dict[gene_id].add(read_name)

gene_ids = sorted(gene_dict, key=lambda x: len(gene_dict[x]), reverse = True)

for gene_id in gene_ids:
	mySet = gene_dict[gene_id]
	num_reads = len(mySet)

	print("{}\t{}".format(gene_id, num_reads))

sys.exit(0)
