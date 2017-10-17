#!/usr/bin/env python3

#import data that is added to the commandline after calling the script $ ./testscript2.py w x y z
import sys

#answers for the questions which are askd by the script
name = sys.argv[1]
colour = sys.argv[2]
hobby = sys.argv[3]
animal = sys.argv[4]

print(name, colour, hobby, animal)

