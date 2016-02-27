#!/usr/bin/python

nums={1,2,1,3,1,4,5,6}
print nums # output: set([1, 2, 3, 4, 5, 6]) radganac ertidaigive mnishvneloba meordeba
		
nums.add(7)
nums.remove(5)
print nums, len(nums)

first = {1,2,3,4,5,6}
second = {5,6,7,8,9,0}

print first | second
print first & second
print first - second 
print second - first
print first ^ second
