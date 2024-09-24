# x = 4
# print(x)

# def hello():
#     x = 5

#     print(f"The local x is {x}")
#     print("Hello Abirlal")

# print (f"The global x is {x}")
# hello()
# print(f"The global x is {x}") 


#----------------------------------------------------------

x = 10 # global variable

def my_function():
    global x
    x = 6
    y = 9 # local variable
    print(9)

my_function()
print(x)
# print(y) # NameError: name 'y' is not defined