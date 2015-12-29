a = open("giga.txt","r") #gaxsnis saxeebi r - wakitxva, w - chawera, wb(rb) - oroboti chawera/walitxva(binary)
print a.readlines()

a.close()#failis daxurva

bfile = open("giga.txt","r")
c = bfile.read(9) #read wakitxvis metodi, romelsac arguments bitebis saxit iRebs, tu ar mivutitebt ramdeni bitis wakitxva gvsurs waikitxavs mtlianad failshi arsebul informacias

file=open("giga.txt","r")
print file.readlines()  #readlines brZaneba ert xazze agiqvams failshi arsebul informacias

for g in bfile:
	print(g), "----"

print c,"######"
giga = len(c)

print c[0] #c shi cawerilia failis pirvel bitze arsebuli informacia

print giga,"*****"

bfile.close()
