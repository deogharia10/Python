dic = {
    10: "Abirlal",
    33: "Arjun",
    45: "Bhaskar",
    67: "Chandan",
}

print (dic[10]) 

# or 

info = {'name':'Abirlal' , 'age':21 , 'eligible': True}
print(info)
print(info['name'])
print(info.get('name')) 

#------------------------- Multiple values ---------------------

nfo = {'name':'Abirlal' , 'age':21 , 'eligible': True}
print(nfo.keys())
print(info.values())

for key in info.keys():
    print(key)

#------------------------ Accessing key value pairs ------------
info = {'name':'Abirlal' , 'age':21 , 'eligible': True}

print(info.items())
for key , value in info.items():
    print(f"The value corresponding to the  key {key} is {value}")