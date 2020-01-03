
def calculateSystem():
    result = 0 
    results = [] 
    remainder = 0 
    remainders = []
    
    number = input("\nType your number: ")
    first_system = int(input("\nType system of this number: "))
    second_system = int(input("\nType system you want: "))

    if first_system != 10:
        for i in range(1, len(number) + 1):
            result += int(int(number[-i]) * (first_system ** (i - 1)))
    else:
        result = number

    checkResults = lambda results : results[-1] >= second_system

    results.append(result)
    remainders.append((result - int(result / second_system) * second_system))

    while checkResults(results):
        results.append(int(results[-1] / second_system))
        remainder = results[-1] - int(results[-1] / second_system) * second_system
        remainders.append(remainder)
    
    finalRes = ''
    for value in reversed(remainders):
        finalRes += str(value)
    
    return finalRes

print(calculateSystem())