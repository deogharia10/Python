#Exercise 12: percentage of Masks
m=int(input("enter the percentage of makas"))
if m<0 and m>100 :
    print("Wrong entry")
elif m>=60 :
    print("Fast division")
elif m>=50 and m<=59 :
    print("Second division")
elif m>=40 and m<=49 :
    print(" Third division")
else :
    print("faill")     