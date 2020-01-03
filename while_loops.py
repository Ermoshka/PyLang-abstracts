curr_number = 0

while curr_number < 10:
    curr_number += 1
    if curr_number % 2 == 0:
        continue
    else:
        print(curr_number)

number = input("type number to check is it even or odd: ")
number = int(number)

if number % 2 == 0:
    print("your number " + str(number) + " is even")
else:
    print("your number " + str(number) + " is odd")

prompt = "\nTell me smth, and i will repeat it back to u"
prompt += "\nEnter 'quit' to the end program: "

active = True
while active:
    msg = input(prompt)
    
    if msg == 'quit':
        active = False
    else:
        print(msg)

while True:
    message = input("\nAnother way with break command: ")

    if message == 'quit':
        break
    else:
        print(message)

# delete duplicte elements
guys = ['erma', 'serega', 'markovka', 'serega', 'jeff']

while 'erma' in guys and 'serega' in guys:
    guys.remove('erma')

print(guys)