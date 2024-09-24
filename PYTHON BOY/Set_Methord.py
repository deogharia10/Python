# ------------------------- Union And Update--------------------------
# s1 = {1, 2, 3, 4, 5}
# s2 ={5, 6, 9}
# s1.update(s2)
# print (s1.union(s2))
# print (s1, s2)

# ------------------------ Intersection ---------------------

s1 = {1, 2, 3, 4, 9, 5}
s2 ={5, 6, 9}

print (s1.intersection(s2))

#------------------------- Symmetric Defference --------------

Town1 = {"Bankura" , "Kolkata" , "Durgapur", "Asansol"}
Town2= {"Durgapur", "Asansol", "Burdwan", "Kolkata"}

Town3 = Town1.symmetric_difference(Town2)
print(Town3)

# ------------------------- Difference And Update-----------------

Town1 = {"Bankura" , "Kolkata" , "Durgapur", "Asansol"}
Town2= {"Durgapur", "Asansol", "Burdwan", "Kolkata"}

Town3 = Town1.difference(Town2)
print(Town3)

# -------------------------- isDisjoint---------------------------
Town1 = {"Bankura" , "Kolkata" , "Durgapur"}
Town2= {"Burdwan", "Kolkata" , "Durgapur"}

print(Town1.isdisjoint(Town2))

#-------------------------- isSuperset----------------------------
Town1 = {"Bankura" , "Kolkata" , "Durgapur" , "Kgp"}
Town2= {"Bankura" , "Kolkata"}
print(Town1.issuperset(Town2))
Town3= {"Kolkata" , "Durgapur"}
print(Town1.issuperset(Town3))

#------------------------ isSubset -------------------------------

Town1 = {"Bankura" , "Kolkata" , "Durgapur" , "Kgp"}
Town2= {"Bankura" , "Kolkata"}
print(Town2.issubset(Town1))
Town3= {"Khatra" , "Durgapur"}
print(Town3.issubset(Town1))

#-------------------------- Add()---------------------------------

Town1 = {"Bankura" , "Kolkata" , "Durgapur"}
Town1.add("Burdwan")
print(Town1)

#------------------------Update()---------------------------------

Town1 = {"Bankura" , "Kolkata" , "Durgapur"}
Town2 ={"Burdwan"}
Town1.update(Town2)
print(Town1)

#----------------------- Remove()/ discard()-----------------------
Town1 = {"Bankura" , "Kolkata" , "Durgapur"}
Town1.remove("Kolkata")
print(Town1)

# Discard dose not raise any error
Town1 = {"Bankura" , "Kolkata" , "Durgapur"}
Town1.discard("Bankura2")

#------------------------pop()-------------------------------------

Town1 = {"Bankura" , "Kolkata" , "Durgapur"}
item = Town1.pop()
print(Town1)
print(item)

#------------------------ Clear()-----------------------------------
Town1 = {"Bankura" , "Kolkata" , "Durgapur"}
Town1.clear()
print(Town1)

#---------------------Check if item Exists-------------------------

Town1 = {"Bankura" , "Kolkata" , "Durgapur"}
if "Kolkata" in Town1: 
    print("Kolkata is present.")
else:
    print("Kolkata is absent.")    






