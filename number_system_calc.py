
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
        result = int(number)

    checkResults = lambda results : results[-1] >= second_system

    results.append(result)
    remainders.append((result - (result // second_system) * second_system))

    while checkResults(results):
        results.append((results[-1] // second_system))
        remainder = results[-1] - (results[-1] // second_system) * second_system
        remainders.append(remainder)
    
    return ''.join([str(value) for value in reversed(remainders)])