# ---------------------- Append Method --------------------
# add to elemant
l= [1,2,3,4,5]
print(l)
l.append(7)
print(l)

# ----------------------- Sort Method ----------------------

l= [11,45,1,2,3,4,5]
print(l)
l.sort()
print(l)

# or
l= [11,45,1,2,3,4,5]
print(l)
l.sort(reverse=True)
print(l)

#-------------------- Reverse Method ----------------------
l= [11,45,1,2,3,4,5]
print(l)
l.reverse()
print(l)


# -------------------- Index Method -----------------------

l= [11,45,1,2,3,4,5,1,1]
print(l)
print(l.index(45))
print(l)

#---------------------- Count Method ----------------------

l= [11,45,1,2,3,4,5,1,1]
print(l)
print(l.count(1))
print(l)

#---------------------- Copy Method ------------------------

l= [11,45,1,2,3,4,5,1,1]
print(l)
m = l.copy()
m[0] = 0
print(l)

#----------------------- Insert Method ---------------------

l= [11,45,1,2,3,4,5,1,1]
print(l)
l.insert(2,10)
print(l)

#----------------------- Extend method ---------------------

m = [100,200,300]
k=l+m
print(k)
# l.extend(m)
print(l)