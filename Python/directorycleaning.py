#Script to search a particular type of file in a directory,print its first line and if required remove the file
import os
from os.path import join

count = 0
for (dirname, dirs, file) in os.walk('.'):
	for filename in file:
		if filename.endswith('.py'):
			thefile = os.path.join(dirname,filename)
			size = os.path.getsize(thefile)
			fhand = open(thefile,'r')
			lines = list()
			for line in fhand:
				lines.append(line)
			fhand.close()
			if len(lines) > 1:
				print(len(lines), thefile)
				print(lines[:1])
		
