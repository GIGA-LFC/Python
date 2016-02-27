#!/usr/bin/python

def addfive(x):
	return x+5

nums = [11,22,33,44,55]
result = list(map(addfive,nums)) #list rom movshalot shedegi igive iqneba
print result

res = list(filter(lambda x: x%2 == 0, nums))  # piroba gvahccvenebs gawerili pirobis shedegs
bla = list(map(lambda x: x%2 == 0, nums)) # moqmedebs pirobis mixedvit
print res, bla
