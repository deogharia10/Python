#Exercise 6:Sum of the digits in an integer
n=(input("enter the 4 digits number :"))
s=0
while (n!=0):
    r=n%10
    s=s+r
    n=n//10
print("sum of digits :",n) 