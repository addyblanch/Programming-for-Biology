#!/usr/bin/env python3

import sys

#Script to reverse complement a DNA sequence

dna = sys.argv[1]

#Performs the complement by changing upper into lower to avoid cyclical conversion
dna_comp = (dna.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c'))

#Converts new lower complement back into upper case
dna_comp_upper = dna_comp.upper()

#Performs the reverse of the complement strand
dna_rev_comp = dna_comp_upper[::-1]

#Prints the three versions incorporating sequence title and primes
print("Original Sequence", "5'", dna, "3'")
print("Complement", "5'", dna_comp_upper, "3'")
print("Reverse Complement", "5'", dna_rev_comp, "3'")
