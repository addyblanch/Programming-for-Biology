#!/usr/bin/env python3

#Script to determine AT GC content of a DNA sequence

import sys

dna = sys.argv[1]

AT_Count = dna.count('A')+dna.count('T')

GC_Count = dna.count('G')+dna.count('C')

Length_of_Seq = len(dna)

AT_Content = AT_Count/Length_of_Seq*100
GC_Content = GC_Count/Length_of_Seq*100

print ("AT Content is" , AT_Content, '%' ,  "and the GC content is", GC_Content , '%')


