import sys

Salary = float(input("Enter Basic salary: "))

if Salary < 20000:
    bonus = Salary*5/100
elif Salary > 20000 and Salary < 40000:
    bonus = Salary*10/100
else:
    bonus = Salary*15/100

print("Basic salary: ",Salary)
print("Annual bonus: ",bonus)
print("total salary: ",Salary+bonus)