file =open("gigenco.txt","w") 		#vxsnit fails chaweris funqciit iqmneba faili
file.write("vwert failshi")  		#vwert failshi informacias
file.close() 				#vxuravt fails

file = open("gigenco.txt","r")		#vxsnit r(wakitxvis) funqciit fails
print file.read()			# vkitxulobt informacias
file.close()


#damatebit 

with open("gigenco.txt") as f:
	print f.read()


