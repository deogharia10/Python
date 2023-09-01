#Exercise 13: Points on a straight light
x1=int(input("enter the x1 :"))
y1=int(input("enter the y1 :"))
x2=int(input("enter the x2 :"))
y2=int(input("enter the y3 :"))
x3=int(input("enter the x3 :"))
y3=int(input("enter the y3 :"))
if x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)==0:
    print ("three points are collineas")
else :
    print("three points are not collineas") 
