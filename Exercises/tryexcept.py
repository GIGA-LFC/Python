
try:
	n1 = 7
	n2 = 0
	print n1/n2 # try funqciashi shsecdomis shemdeg arsebuli brdzaneba agar iqneba aqtiuri programa gadava except nawilze
except ZeroDivisionError: #faqtorebi romlebis moxdenis(specialurad an gautvaliswineblad) shemtxvevashi exceptit Segvidzlia reagirebis moxdena
	print "0 ze gayofa"," ar SeiZleba! "
except(ValueError, TypeError):
	print "Secdoma"
except: #rodesac ar vicit shecdomis tipi
	print 'shecdoma'
