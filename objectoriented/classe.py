class hero:
	def __init__ (self, name):
		self.name = name
		self.health = 100
	def eat(self,food):
		if (food == 'apple'):
			self.health -= 100
		elif (food == 'ham'):
			self.health += 20

person = hero("Bob")
print "name = ", person.name, "health = ", person.health
person.eat('apple')
print "health = ", person.health
person.eat('ham')
print "health = ", person.health


