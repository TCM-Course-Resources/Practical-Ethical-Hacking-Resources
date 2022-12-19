from Shoes import Shoes

low = Shoes('And 1s', 30)
medium = Shoes('Air Force 1s', 120)
high = Shoes('Off Whites', 400)

try:
    budget = float(input('What is your budget? '))
except ValueError:
    exit('Please enter a number')

for shoes in [high, medium, low]:
    shoes.buy(budget)
