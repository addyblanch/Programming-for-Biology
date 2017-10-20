#!/usr/bin/env python3

import re

fasta_headers = open ('Python_06.fasta','r')

#Searches fasta file using regex to print out headers
#parts of regex in () are groups
for line in fasta_headers:
	found = re.search(r"^(>\S+)(\s?.*)", line)
	if found:
		print("id", found.group(1), "description", found.group(2))

