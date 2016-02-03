class hero: #klasis araswori argumentis motxovnisas, anu mtavari programidan tu klasis ararsebul wevrsv vitxovt am shemtxvevashi xdeba "  AttributeError  "
	def __init__ (self, name):
		self.name = name
		self.health = 100
	def eat(self,food):
		if (food == 'apple'):
			self.health -= 100
		elif (food == 'ham'):
			self.health += 20

class cat:
	age = 5
	def __init__(self, color, leg):
		self.color = color
		self.legs = leg
	def bark(self):
		print "boom!"

felix = cat("ginger",4)
fido = cat("green", 4)

print "Fido's age is", cat.age, " and have", fido.legs, " legs"
print "felix is ", felix.color
felix.bark()

person = hero("Bob")
print "name = ", person.name, "health = ", person.health
person.eat('apple')
print "health = ", person.health
person.eat('ham')
print "health = ", person.health


