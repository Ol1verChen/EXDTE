#get input

#ask user for name

name = input('Hello there! What is your name? ')

#ask user for 2 numbers

number1 = int(input('Give me a number: '))
number2 = int(input('Give me another number: '))

#add numbers together

add = number1 + number2
print("{} + {} = {}".format(number1, number2, add))

#multiply numbers together

multiply = number1 * number2
print("{} * {} = {}".format(number1, number2, multiply))

#greet user

print(f'Nice to meet you {name}.')