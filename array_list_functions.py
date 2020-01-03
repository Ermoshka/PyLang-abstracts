bicycles = ['trek', 'cannondale', 'redline', 'specialized']

# add element at the end
bicycles.append('illusion')

# insert element
bicycles.insert(2, 'bmx')

# removing by index
del bicycles[3]

# removing by value
bicycles.remove('cannondale')

# removing last el and get it
last = bicycles.pop()

# sorting by integer and alphabetically by string
numbers = [4, 2, 5, 9, 2, 1]
numbers.sort()
print(numbers)

# temporary sorting
newNumbers = [3, 1, 5, 7, 6, 2, 4]
print(sorted(newNumbers), newNumbers)

# reverse elements
numbers.reverse()
print(numbers)

# slice elements:  [:2] are first two elements and [2:] are last elements to the second, while [-2:] are last two elements
name = 'Ermakhan'
length = len(name)
print(name[:2], name[-2:])
# from 2 position to the last first position
print(name[2:-1])
# an and makhan
print(name[-2:], name[2:])

