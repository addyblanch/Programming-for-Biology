#!/usr/bin/env python3

#Script to interate through a list

nums = [101,2,15,22,95,33,2,27,72,15,52]

odd = 0
even = 0

for num in nums:
	if num%2 == 0:
		even+=num
	else:
		odd+=num
print(odd)
print(even)
