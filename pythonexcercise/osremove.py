#!/usr/bin/python
import os
myfile="/home/gigenco/Documents/pythonexcercise/osremove.py~"
 
## if file exists, delete it ##
if os.path.isfile(myfile):
	os.remove(myfile)
	print "washla", "faili",myfile
else:    ## Show an error ##
	print("ar waishala",myfile)
 
