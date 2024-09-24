Countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(Countries)
temp.append("Russia") # add item
temp.pop(3)           # remove item
temp[2] = "Finland"   #change item
Countries = tuple(temp)
print(Countries)

# or

countries1 = ("A", "B", "C", "D")
countries2 = ("V", "X", "Y", "Z")
countriesAlphabet = countries1 + countries2
print(countriesAlphabet)

#---------------------- Count method ----------------------

tuple = (0,1,2,3,5,3,6,3,4,5,6,5,7,5,9)
res = tuple.count(5)
print("Count of 5 tuple is:", res)

#--------------------- Index method ----------------------

tuple = (0,1,2,3,5,3,6,3,4,5,6,5,7,5,9)
res = tuple.index(3)
print("Count of 5 tuple is:", res)
