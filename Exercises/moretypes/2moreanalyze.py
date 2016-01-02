#!/usr/bin/python

def cchar(text,letter):
	count = 0
	for c in text:
		if c == letter:
			count +=1
	return count

filename = input("filename: ")
with open(filename) as f:
	text = f.read()

for char in "qwertyuioplkjhgfdsazxcvbnm":
	perc = (100 * cchar(text,char))/len(text)
	print "{0}---{1}%".format(char,round(perc,2)) # to reduce the number of digits printed 4 nishna ricxvistvis argumenti tua 2 2 erteulis shemdeg wers mdzimes, 3 ianis shemtxvevashi 3 erteuli shemdeg
	a = 0	
	a = a+perc	
print a
