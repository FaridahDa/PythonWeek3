#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

print((len(Belgium)) * "-")

Belgium_update = Belgium.replace(",", " : ")
print(Belgium_update)

Belgium_list = list(Belgium_update.split(","))
print(Belgium_list)

Belgium_pop = Belgium_list[2]
Brussel_pop = Belgium_list[6]
print(Belgium_pop + Brussel_pop)

# finish
#convert string to list

#print(Bel)