#!/bin/python3

## --------- Reading --------- ##
months = open('months.txt')

# print(months.read())
# print(months.readline()) # read one line
# print(months.readlines()) # read all lines
print(months.read())
# months.seek(0) # return to first line 
# print(months.read())

# months.seek(0) # return to first line 
# print("Print Using For loop ")
# for month in months:
#     print(month)

# months.seek(0) # return to first line 
# print("Print Using For loop with strip method")
# for month in months:
#     print(month.strip())

months.close()

## --------- Writing --------- ##

# arg 'w' for writing (overwrite), arg 'a' for append
days = open('days.txt', "a")

days.write("Monday")
days.write("\nMonday") # '\n' fo new line 

days.close()
