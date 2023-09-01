#Exercise 11: Employee Salary
bs= int(input("enter the salary :"))
if bs<1500:
    HRA=bs*0.1
    DA=bs*0.9

else:
    HRA=500
    DA=bs*0.98
g_salary= bs+HRA+DA
print("the gross salary :", g_salary)