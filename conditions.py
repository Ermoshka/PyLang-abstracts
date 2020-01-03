cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars[1:]:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# check existing condition in arrays
if 'audi' in cars:
    print('Yeah it exists!')

if 'bentley' not in cars:
    print('i wanna cry')

# if-elif-else
my_age = 18

if my_age < 18:
    print('i can\'t sell you it')
elif my_age == 18:
    print('it\'s wonderful being adult')
else:
    print('gimme my money')


