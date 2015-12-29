#!/usr/bin/python

f = open('workfile', 'w') # vqmnit fails
f.write("this is first line ")	#failshi vwert teqsts
value =('ansver', 42)	
s = str(value) #str funqcia romelic s-s anichebs valueshi arsebul informaciasmiuxedavad gansxvavebuli cvladebis
f.write(s) #fails davamatet damatebiti teqsti
print f

f = open('workfile', 'r+') # xelaxla gailis gaxsnisas cursori brundeba dasawyisshi
f.seek(33) #kursori gadagvaqvs 33 baitit
f.write('0123456789abcdef') #am baitidan viwyebt sxva informaciis damatebas
f.write('giga')# am shemtxvevashi kursori boloshia da kidev emateba informacia

f.seek(33)
print f.read(5) #araperi daibeWdeba radgan kursoris shemdeg araperi weria/ 5 baitis shemdeg

#am shemtxvevashi kursori gadaiwia 38-e baitze

f.seek(-4,1) # pirveri argumenti kursoris gadaadgilebaa(konkretuli mdebareobidan -marcxniv +marjvniv) im raodenobis bitebze rasac davwert, meores 1/2 romelime informacia gadaecema 1 iansi shemtxvevashi gadaadgildeba manamde arsebuli misamartidan, xolo 2 ianis shemtxvevashi bitebis atvla iwyeba bolo misamartidan
print f.read()


