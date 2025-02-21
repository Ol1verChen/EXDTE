#If State & While loops

#We can use 'if' statements to execute code if a given condition is set
#To check if two variable are the same we use DOUBLE equals (==)
#Python is case sensitive. 'Hello' is not the same as 'hello'
#We can get around this by using .lower()
#While loops are useful when we want the program to loop until a given condition is met but we don't know
#How many times it needs to loop

#If statement

keep_going = ''
while keep_going == '':

 coffee = input('Do you like coffee? ').lower()

 if coffee == 'yes' or coffee == 'y':
    print('I like coffee too!')
 elif coffee == 'no'or coffee == 'n':
    print('You are a weirdo.')
 else:
    print('I asked you a yes or no question...')
    
 keep_going = input ('I will give you another more chance...')
 print()
 

 
# Press <enter> to contunue or any key to quit