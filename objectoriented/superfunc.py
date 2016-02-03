class A:
	def spam(self):
		print (1)

class B(A):
	def spam(self):
		print (2)
		super().spam() # super metodi idzaxebs yvela motxovnil metodebs sadac sheudzlia edzebs, arsebul da mshobel klasebshi

B().spam()
