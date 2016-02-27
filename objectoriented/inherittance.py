class animal:
	def __init__(self, name, age, color):
		self.name = name
		self.age = age
		self.color = color
class cat(animal):
	def felix(self):
		print "felix"
class dog(animal):
	def miki(self):
		print "boom"

class wolf:
	def __init__(self, name, color):
		self.name = name
		self.color = color
	def bla(self):
		print "brr..."
class Dog(wolf):
	def bla(self):
		print "woof!"

husky = Dog("max","grey")
husky.bla()

fido = dog("fido", 4, "brown")
print fido.color, " & ", fido.age, " & ", fido.name
fido.miki()

