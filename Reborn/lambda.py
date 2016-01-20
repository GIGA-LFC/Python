#!/usr/bin/env python


def func (f, arg):
	print f(arg) #  f, igebs funqciis mnishvnelobas, gadaecema argumenti 5. fnqcia 4*5*5 igebs mnishvnelobas
	return f(arg)

func(lambda x: 4*x*x, 5) 


def bla(x):
	return x**2+5*x+4 

print bla (-4)

print (lambda x: x**2+5*x+4)(-4) #lambdas aketebs punqciis msgavs davalebas mcire mnishvnelobit, araa misi agwera kodis sxva nawilshi

double = lambda x: x*3

print double(7) #cvladi romelic igebs punqciis mnishvnelobas
