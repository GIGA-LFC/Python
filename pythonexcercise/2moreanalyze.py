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

for char in "abgdevztiklmnopjrstu":
	perc = (100 * cchar(text,letter))/len(text)
	print "{0}---{1}%".format(char,round(perc,2))
