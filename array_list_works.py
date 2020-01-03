names = ['ermakhan', 'sabyrzhan', 'talgatuly']
full_name = ''

for name in names:
    full_name += name + ' '

print(full_name.title())

# prints from 1 to 4
for value in range(1, 5):
    print(value)

some_numbers = []

for number in range(1, 11):
    newNumber = number ** 2 # number to the power of 2
    some_numbers.append(newNumber)

print(some_numbers)

# sample statistics
minN = min(some_numbers)
maxN = max(some_numbers)
sumN = sum(some_numbers)

print(minN, maxN, sumN)

# list comprehension or generator

numbersList = [value ** 2 for value in range(1, 11)]
print(numbersList)

# Ermakhan Sabyrzhan
for name in names[:2]:
    print(name.title())

# Copy array
my_foods = ['pizza', 'sushi', 'lagman']
fav_foods = my_foods[:]

# tuples, immutable array's variables (doesn't support item assignment) but you can change whole tuple
dimensions = (23, 20, 19)
dimensions = (19, 20, 21)
# dimensions[1] = 22 returns type error

