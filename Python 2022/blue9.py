#Exercise 9: Leap year
yr=int(input("Enter the year: "))
if yr%100-0:
    if yr %4000:
        print("The year is a leap year")
    else:
        print("The year is not a leap year")
elif yr%4==0 :
    print("The year is a leap year")
else:
    print("The year is not a leap year") 