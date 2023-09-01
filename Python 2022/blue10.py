#Exercise 10: Discount Calculation on 1000 itemes
total=0
count=1
x=-999
while(True):
    if count>1:
        x=int(input("Enter 1 to continue, e to exit :"))
    if x==0:
        break
    q=int(input("Enter the quantity of the product : "))
    p=int(input("Enter the price of the product :")) 
    total=total+(q*p)
    count=count+1
if total>=1000:
    total=total*0.9
print("The total amount",total)    