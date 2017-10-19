#!/usr/bin/env python3

#file_read opens file to collect data from
#file_write creates file to wirte new data too

file_read = open('Python_05.txt', 'r')
file_write = open('Python_05_uc.txt', 'w')

#for loop to take each line from file_read convert to capitals and insert into new file_write

for line in file_read:
	file_write.write(line.upper())

#closes both files
file_read.close()
file_write.close()

#prints to stout that file was created
print("Created 'Python_05_uc.txt'")
