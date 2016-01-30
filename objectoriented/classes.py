#!/usr/bin/python

class cat:
	def __init__(self, color, legs):  # __init__ aris konstruqtori anu init punqcia iRebs default mnishvnelobebs rasac chven gavuwert, am shemtxvevashi color da leg cvladebi arian default mnishvnelobis mqoneni
		self.color = color # self  klashi public da private mnishvnelobebs gansazRvravs	
		self.legs = legs # anu self.bla wertilis shemdeg cvladi xdeba public da shegvidzlia mivmartot mtavari punqciidan, tu self. ar ewereba cvlads win mas ver mivmartavt sxva punqciidan
	def pc(self):
		print 'cat'


felix = cat("ginger",4)

rover = cat("black",4)

miau = cat("brwon",3) 
print miau.color
miau.pc()
