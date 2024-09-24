# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is: ")

# try:
#     for i in range (1,11):
#         print(f"{int (a)} * {i} = {int(a)*i}")

# except:
#     print(" Invalid Input")

try:
    nam = int(input("Enter an integer: "))
    a=(6, 3)
    print (a[nam])

except ValueError:
    print("Number  is not an integer")

except IndexError:
    print("Index Error")    
