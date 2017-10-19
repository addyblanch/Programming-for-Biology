#!/usr/bin/env python3

#opens file in read only mode
file = open("Python_05.txt", "r")

#for loop to convert text into capitals and remove white space introduced using print()

for line in file:
	print(line.upper(), end= '')
