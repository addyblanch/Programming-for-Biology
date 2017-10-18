#!/usr/bin/env python3

#Script to determine AT content of a DNA sequence

import sys

dna = sys.argv[1]

AT_Count = dna.count('A')+dna.count('T')

Length_of_Seq = len(dna)

AT_Content = AT_Count/Length_of_Seq*100

print (AT_Content)
