#!/usr/bin/python

kvadrati = {2:4,3:"error",1:1,4:16}
kvadrati[8]=64
kvadrati[5]=25
kvadrati[3]=9


print kvadrati #zedadobit alagebs agweril elementebs

print (5 in kvadrati),(7 not in kvadrati),(16 in kvadrati)
print kvadrati.get(2,"napovnia"), kvadrati.get(123," 123-is msgavsi ar moidzebna ")#get-i gvadlevs (argumentis)mnishvnelobas im cvladidan rastanac vwert. tu pirveli argumentis mnishvnelobis shesabamisi mnishvneloba ver ipova meore argumentis mnishvnelobas igebs

list = ["one","two"]

dict ={1:"one","two":2}

tuple = ("tree","four")

my_tuple = "zero","one","two"

print list,dict,tuple,my_tuple[0]
