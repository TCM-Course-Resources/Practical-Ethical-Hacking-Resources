#!/bin/python3

name = input("Enter your name: ")
print("Hello, Mr. " + name)

# calculator #

FIRST_NUMBER = float(input("Enter a number: "))
OPERATOR = input("Enter an operator: ")
SECOND_NUMBER = float(input("Enter another number: "))

if OPERATOR == "+":
    print(FIRST_NUMBER + SECOND_NUMBER)

elif OPERATOR == "-":
    print(FIRST_NUMBER - SECOND_NUMBER)

elif OPERATOR == "*":
    print(FIRST_NUMBER * SECOND_NUMBER)

elif OPERATOR == "/":
    print(FIRST_NUMBER / SECOND_NUMBER)

elif OPERATOR == "**" or OPERATOR == "^":
    print(FIRST_NUMBER ** SECOND_NUMBER)
else:
    print("Unknown operator.")


