#!/usr/bin/python
import datetime

now = datetime.datetime.now()

a = 1
b=a+1
c=a+b

giga = (a, 'saxeli', b ,'gvari', c , 'metsaxeli')

x = repr(giga)
y = str(giga)

print str(now),"******",repr(now)  #igive  funqciis mqone punqciebi titqmis, str - mtlian informacias igebs stringis saxit, repr - c igives aketebs ogond aramarto mtlian informacias igebs aramed damatebit informaciasac tu ra saxisaa informacia

print len(y),len(x)
print x," --- ",y
