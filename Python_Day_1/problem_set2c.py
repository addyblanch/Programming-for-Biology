#!/usr/bin/env python3

# Script to test statement including True/False, positive <> 50, is it even or divisiable by 3

import sys

var = int(sys.argv[1])

if var > 0:
	if var < 50:
		if var % 2==0:
			message = 'this is positive, less than 50 and even' 
			print(var, message)
		else:
			message = 'this is positive odd  number less than 50'
			print(var, message)	
	elif var > 50:
		if var % 3 == 0:
		
			message = 'this is positive, larger than 50 and divisible by three'
			print(var, message)
		else:
			message = 'this is a positive number, greater than 50 not divisable by three'
			print(var, message)

else:
	print('must be a negative number')
