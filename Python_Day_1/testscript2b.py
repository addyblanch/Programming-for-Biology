#!/usr/bin/env python3

#import data that is added to the commandline after calling the script $ ./testscript2.py w x y z
import sys

#answers for the questions which are askd by the script
print('My name is', sys.argv[1])
print('My favourite colour is', sys.argv[2])
print('My favourite hobby is', sys.argv[3])
print('My favourite animal is', sys.argv[4])

