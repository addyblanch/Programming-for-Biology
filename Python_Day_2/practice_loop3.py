#!/usr/bin/env python3

seq = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

for index,seqid in enumerate(seq):
	Length = len(seqid)

	print('Seq ID', index, 'has the Sequence', seqid, 'and a length of', Length)
