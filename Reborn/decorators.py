#!/usr/bin/python

def decor(func):

	def wrap():
		print "----"
		func()
		print "----"
	return wrap

def print_txt():
	print "hello"

decorated = decor(print_txt)
decorated()

