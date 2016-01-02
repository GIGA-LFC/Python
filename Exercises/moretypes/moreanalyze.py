#!/usr/bin/python


def c_char(text,letter):
	count = 0
	#print "----"
	for c in text:
		if c == letter:
			count += 1
			print c
	return count

a = input("enter filename: ")

with open(a) as f:

	text = f.read()

print c_char(text,"i") # failshi konkretuli simbolos raodenobas tvlis

