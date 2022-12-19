#!/bin/python3

from Employees import Employees

employee_1 = Employees("Bob", "Sales", "Director of sales", 10000, 20)

employee_2 = Employees("Linda", "Executive", "CIO", 15000, 10)

print(employee_1.name)
print(employee_1.retirement())


