#!/usr/bin/env python3

import sys

#Script to find restriction site for EcoR1

dna = sys.argv[1]

EcoR1 = 'GAATTC'

restriction_co = dna.find(EcoR1)-1

Frag_one = dna[0:394]

Frag_two = dna[394:]

F1_len = len(Frag_one)

F2_len = len(Frag_two)

string = "This fragment {} starts at base {} and is {} nucleotides long. This fragment {} starts at base {} and is {} nucelotides long"
print(string.format(Frag_one,"0",F1_len,Frag_two,"394",F2_len))


