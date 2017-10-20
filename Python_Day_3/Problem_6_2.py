#!/usr/bin/env python3

import re

poem = open ('Python_06_nobody.txt','r')
new_poem = open ('Python_06_someone.txt', 'w')

for line in poem:
	new = re.sub("Nobody", "Rebecca", line)
	new_poem.write(new)
