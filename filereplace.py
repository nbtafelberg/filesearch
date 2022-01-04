# in file search and replace 
# Paul Clevett 4th Jan
# input arguments  searchandreplace.py searchfortext replacefortext

import os
import glob
import sys


def doReplace(searchword,replacewith):
	root_dir=os.getcwd()
	for filename in glob.iglob(root_dir + '**/**', recursive=True):
		try:
			f = open(filename,'r')
			filedata = f.read()
			f.close()
			newdata = filedata.replace(searchword,replacewith)
			f = open(filename,'w')
			f.write(newdata)
			f.close()
			print("Updating "+filename)
		except UnicodeDecodeError:
			print(filename+ "is not a text file")
		except IsADirectoryError:
			print("Directory "+filename)




import sys

if len(sys.argv)<3:
	print ("In file python search and replace, format filereplace.py searchtext replacetext (don't frget to escape spaces)")
else:
	print ("Searching for "+sys.argv[1]+" replacing with  "+sys.argv[2])
	doReplace(sys.argv[1],sys.argv[2])

