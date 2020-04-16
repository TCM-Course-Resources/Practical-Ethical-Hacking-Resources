#!/usr/bin/env python3

import sys  # import sys library
from datetime import datetime as dt # importing date time and aliasing it as dt
print(sys.version)
print(dt.now())

# Advanced strings
my_name = "Heath"
print(my_name[0])
print(my_name[-1])

sentence = "This is indeed a sentence"
print(sentence[:4])

print(sentence.split())

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)

quote = "He said, \"Give me all your money\""
print(quote)

too_much_space = "          hello"
print(too_much_space.strip())

print ("a" in "Apple")

letter = "A"
word = "Apple"
print(letter.lower() in word.lower()) 

movie = "The Hangover"
print("My favorite movie is {}".format(movie))

# Dictionaries
drinks = {"White Russian":7, "Old Fashion":18, "Lemon Drop":8} #drink is key, price is value
print(drinks)

employees = {"Finance":["Bob", "Linda", "Tina"], "IT":["Gorge", "Louis", "Teddy"], "HR":["Jimmy Jr.", "Mort"]}
print(employees)

employees['Legal'] = ['Mr. Frond'] # add key value pair
print(employees)

employees.update({"Sales":["Andie", "Ollie"]}) # add new key value pair
print(employees)

print(drinks.get("White Russian"))
