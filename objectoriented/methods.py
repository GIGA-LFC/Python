class a:
	def method1(self):
		print "method first"
class b(a):
	def method2(self):
		print "second method"
class c(b):
	def method3(self):
		print "third method"

c=c() # am shemtxvevashi c klass aqvs sxva zemot arsebuli klasebis metodebtan wvdoma sxvebs ara
c.method1()
c.method2()
c.method3()
