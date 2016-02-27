#!/usr/bin/python

def factorial(x):
	if x == 1:
		return 1
	else:
		return x*factorial(x-1)

print factorial(5)


def even (x):
	if x==0:
		return True
	else:
		return odd(x-1)

def odd(x):
	return not even(x)


print odd(17)

print even(23)
