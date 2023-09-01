#Exercise 15:Write a program that finds the average of first n number using a for loop
n=int(input("Enter n : "))
sum=0
for i in range (0,n):
    num=int(input("Enter an integer :"))
    sum=sum+num
avg=sum/n
print("Average = ",avg)    