#!/bin/usr/python


n = [33,43,1,23,55]

if all([i>5 for i in n]):
	print "all large than 5", #n-is yvela mnishvnelobas adarebs 5 s da tu yvela metia if piroba imushavebs

if any([i%2==0 for i in n]):
	print "aris luwi n shi\n", #isev yvela mnishvnelobas adarebs da tu romelime gaamartlebs pirobas if imushavebs

for v in enumerate(n):
	print v # n shi shsemaval misamartze arsebul mnishvnelobas achvenebs
