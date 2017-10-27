#!/usr/bin/env python3

import sys

usage = "\n\n\tusage: kmer_length fastq top_kmers\n\n\n".format(sys.argv[0])

if len(sys.argv) < 4:
	sys.stderr.write(usage)
	sys.exit(1)


kmer_length = int(sys.argv[1])
fastq = sys.argv[2]
top_kmers = int(sys.argv[3])

fastq = open(sys.argv[2], 'r')

line_num = 0
kmers = {}

def count_kmers(kmers, sequence, kmer_length):
	for nt in range(0,len(sequence)-kmer_length+1):
		kmer = sequence[nt:nt + kmer_length]	
		
		if kmer in kmers:
			kmers[kmer] +=1
		else:
			kmers[kmer] = 1


for line in fastq:
	line = line.rstrip()
	line_num += 1
	if line_num % 4 == 2:
		count_kmers(kmers, line, kmer_length)

top_kmers = sorted(kmers, key = lambda x:kmers[x], reverse = True)[0:top_kmers]
for item in top_kmers:
	print("{}\t{}".format(item, kmers[item]))
