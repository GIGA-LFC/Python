#!/usr/bin/python

print '{0} and {1}'.format('giga','lalu')

table = {'giga':4127, 'lalu':4098, 'gigenco':7678}
for name, phone in table.items():
	print '{0:10} ==> {1:10d}'.format(name, phone)
	print name," ---- ",phone
