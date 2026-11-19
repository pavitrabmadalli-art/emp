import sys

salary = float(sys.argv[1])

if salary < 20000:
    bonus = salary * 5 / 100
elif salary < 40000:
    bonus = salary * 10 / 100
else:
    bonus = salary * 15 / 100

print("Basic salary:", salary)
print("Annual bonus:", bonus)
print("Total salary:", salary + bonus)