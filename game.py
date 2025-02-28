import random

# Introduce the user to the game
bank_balance = float(3512)
owe_to_bank = 0
pay = 1

print('Welcome to the Rototuna Charity!')
name = input('Enter full name: ')
if name == '':
    print("Your name isn't nothing is it?")
    name = input('Enter full name: ')
siblings = input('How many sibling(s): ')
if siblings == '':
    print('At least put down 0!')
    siblings = input('How many sibling(s): ')
best_friend = input("Best friend name: ")
if best_friend == '':
    print('No best friend? So sad.')
elo = input('What is your Elo on chess.com: ')
if elo == '':
    print("Don't play chess? Fair enough.")
mc_account = input('Minecraft account address: ')
if mc_account == '':
    print("Don't tell me you don't play Minecraft...")
else:
    mc_account_password = input('Password to Minecraft account: ')
    if mc_account_password == '':
        print('Come on, no reason to be shy.')
        mc_account_password = input('Password to Minecraft account: ')
bank_account = input('Please enter your bank account details here: ')
if bank_account == '':
    print('This is essential')
    bank_account = input('Please enter your bank account details here: ')
    if bank_account == '':
        print('Not gonna work again.')
        bank_account = input('Please enter your bank account details here: ')
        if bank_account == '':
            print('Fine, you asked for it...')
            bank_balance = float(2500)
            owe_to_bank = owe_to_bank + 50000
else:
  pin = input('Enter your pin here: ')
  if pin == '':
      print('Fair enough.')
      bank_balance = float(2500)
      owe_to_bank = owe_to_bank + 50000
  else:
      card = input('Enter your card number here: ')
      if card == '':
        print('Fair enough.')
        bank_balance = float(2500)
        owe_to_bank = owe_to_bank + 50000
address = input('Address here: ')
if address == '':
    print('(This is needed for the game to work!)')
    address = input('Address here: ')
social = input('Social security number here: ')
if social == '':
    print('You are a lazy person.')
email = input('Email address: ')
if email == '':
    print('Is this getting annoying?')
else:
    password_email = input('Password to your email: ')
    if password_email == '':
        print('Password incorrect!')
        print('Try again')
        password_email = input('Password to your email: ')
        if password_email == '':
            print('It is not that hard.')
            password_email = input('Password to your email: ')
            if password_email == '':
                print('Alright, it is fine, I get it.')
                bank_balance = float(2500)
                owe_to_bank = owe_to_bank + 50000

# The decision of a lifetime...

print("By entering 'yes', you are agreeing that we can sell your legal informations if we need to.")
print('We are NOT responsible for you losing all your money')
print('You are not allowed to leave until we say so...')
proceed = input('Do you wish to start playing (yes / no)? ').lower()
if proceed == 'yes':
    print('Good choice!')
elif proceed == 'no':
    print('You are playing anyways')
else:
    print("I don't get paid enough for this okay?")
    
# Rules of the game

separator = ('-------------------------------------------------------------------------------------------------------------------------------------------------------')
print(separator)
print('Rules of the game:')
print(separator)
print('Pay $1.00 to play and draw a token to determine if you win')
print(separator)
print('')
print(separator)
print('Chances of drawing each token:')
print('Unicorn = 20.0%')
print('Zebra / horse = 30.0%')
print('Donkey = 20.0%')
print(separator)
print('')
print(separator)
print('Every game will cost you $1.00')
print(separator)
print('Unicorn = $5.00')
print('Zebra = $0.50')
print('Horse = $0.50')
print('Donkey = Nothing')
print(separator)

# Bank balance & ACTUAL winning chances

deposit = float(input('How much money are you depositing?(According to your bank account, you have $3512.00): '))
if deposit > bank_balance:
    print('You are trying to withdraw more than what you have!')
    print('The rest of the money will be taken from the bank (you have to pay back)')
    owe_to_bank = deposit - bank_balance
elif deposit < bank_balance:
  print(f'You have withdrawn ${deposit}0 from your bank balance to play the game')
  bank_balance = bank_balance - deposit
  print(f'You have ${bank_balance}0 left in your bank balance.')

# Playing the game

print(f'You have ${deposit}0 in your balance')

keep_playing = ''
while keep_playing == '':
 play = input('Press <enter> to start playing!')
 if play == '':
   deposit = deposit - pay  
   random_number = random.random()
   if random_number <= 0.0001:
       print('You drew a Mega Unicorn!!!')
       print('You just won $100.00!')
       deposit = deposit + 100
   elif random_number <= 0.0002:
       print('You drew an Unlucky Unicorn')
       print('You lost $5,000.00')
       deposit = deposit - 5000
   elif random_number <= 0.0004:
       print('You drew a Unicorn!!')
       print('You just won $5.00! ')
       deposit = deposit + 5
   elif random_number <= 0.03:
       print('You drew a Dinosaur!')
       print('Something has happened...')
   elif random_number <= 0.05:
       print('You drew a Zebra!')
       print('You won $1.00')
       deposit = deposit + 1
   elif random_number <= 0.07:
       print('You drew a Rubix cube...')
       random_question_addition1 = random.random()
       random_question_addition2 = random.random()
       addition_solver = random_question_addition1 + random_question_addition2
       answer_addition = float(input(f'What is {random_question_addition1} + {random_question_addition2}: '))
       if answer_addition == addition_solver:
           print('You solved the equation correctly!')
           print('You are rewarded with $10.00')
           deposit = deposit + 10
       elif answer_addition == '':
           print('Woah, not too fast!')
       else:
           print('Incorrect!')
           print('As a punishment, $20.00 has been taken from your balance...')
           deposit = deposit - 20
   elif random_number <= 0.071:
       print('You drew a horse!')
       print('You won $0.50!')
       deposit = deposit + 0.5
   elif random_number <= 0.08:
       print('You drew a Squid...')
       random_question_subtraction1 = random.random()
       random_question_subtraction2 = random.random()
       subtraction_solver = random_question_subtraction1 - random_question_subtraction2
       answer_subtraction = float(input(f'What is {random_question_subtraction1} - {random_question_subtraction2}: '))
       if answer_subtraction == subtraction_solver:
           print('You solved the equation correctly!')
           print('You are rewarded with $15.00')
           deposit = deposit + 15
       elif answer_addition == '':
           print('Woah, not too fast!')
       else:
           print('Incorrect!')
           print('As a punishment, $25.00 has been taken from your balance...')
           deposit = deposit - 25
   elif random_number <= 0.09:
       print('You drew a Fish...')
       random_question_multiplication1 = random.random()
       random_question_multiplication2 = random.random()
       multiplication_solver = random_question_multiplication1 * random_question_multiplication2
       answer_multiplication = float(input(f'What is {random_question_multiplication1} * {random_question_multiplication2}: '))
       if answer_multiplication == multiplication_solver:
           print('You solved the equation correctly!')
           print('You are rewarded with $20.00')
           deposit = deposit + 20
       elif answer_addition == '':
           print('Woah, not too fast!')
       else:
           print('Incorrect!')
           print('As a punishment, $30.00 has been taken from your balance...')
           deposit = deposit - 30
   elif random_number <= 0.1:
       print('You drew a Donkey!')
       print('You win nothing.')
   elif random_number <= 0.10885:
       print('You drew a Brick!')
       print('You now owe the bank an additional $100.00')
       owe_to_bank = owe_to_bank + 100
   elif random_number <= 0.15:
       print('You drew a Snake!')
       print('$35.00 has been taken from your balance for no reason!')
       deposit = deposit - 35
   elif random_number <= 0.24945:
       print('You drew a Goose...')
       random_question_division1 = random.random()
       random_question_division2 = random.random()
       division_solver = random_question_division1 / random_question_division2
       answer_division = float(input(f'What is {random_question_division1} / {random_question_division2}: '))
       if answer_division == division_solver:
           print('You solved the equation correctly!')
           print('You are rewarded with $25.00')
           deposit = deposit + 25
       elif answer_addition == '':
           print('Woah, not too fast!')
       else:
           print('Incorrect!')
           print('As a punishment, $35.00 has been taken from your balance...')
           deposit = deposit - 35
           
       
 print(f'You have ${deposit}0 left in your balance')
 
 # Checking if balance goes to or below 0
 
 if deposit <= 0:
    print('You have ran out of money in your balance!')
    owe_to_bank = owe_to_bank + deposit
    if bank_balance > 0:
      withdraw_2 = input('Would you like to withdraw money from your bank? (yes / no) ').lower() # Still have money left in bank account
      if withdraw_2 == 'yes':
          withdraw_from_balance = float(input(f'How much would you like to withdraw? (You have ${bank_balance}0 left in your bank account): '))
          if withdraw_from_balance > bank_balance:
              print('You are trying to withdraw more than what you have!')
              print('The rest of the money will be taken from the bank (you have to pay back)')
              deposit = deposit + 5000 # You now owe the bank
              pay = pay + 14
          elif withdraw_from_balance < bank_balance:
              print(f'You have withdrawn ${withdraw_from_balance}0 from your bank account.')
              deposit = deposit + withdraw_from_balance
              bank_balance = bank_balance - withdraw_from_balance
              print(f'You have ${bank_balance}0 left in your bank balance.')
              pay = pay + 14
    elif bank_balance < 0:
        sell_house = input('Would you like to sell your house for $25,000.00? (yes / no) ').lower() # No more money left in bank account
        if sell_house == 'yes':
             deposit = deposit + 25000
             owe_to_bank = owe_to_bank + 20000 # Simply taxes
             pay = pay + 14
             sell_car = input('Would you also like to sell your car for $30,000.00? ').lower()
             if sell_car == 'yes':
               deposit = deposit + 30000
               owe_to_bank = owe_to_bank + 25000 # Simply taxes
               pay = pay + 14
             elif sell_car == 'no':
                print('We can help you borrow $8,000.00 from your bank account on your behave.') # You now owe the bank
                owe_to_bank = owe_to_bank + 8000
                pay = pay + 14
             else:
                 print('That is too bad')
                 deposit = deposit + 10000 # You now owe the bank
                 owe_to_bank = owe_to_bank + 10000
                 pay = pay + 14
        elif sell_house == 'no':
          print('We will help you borrow $5,000.00 from your bank account on your behave.') # You now owe the bank
          deposit = deposit + 5000
          pay = pay + 14
        else:
          print("I said I don't get paid enough for this!")
          deposit = deposit + 10000 # You now owe the bank
          pay = pay + 14

# The ending

if deposit <= 0:
    if bank_balance <= 0:
        print('You have ran out of money...')
        print('Oh well, at least its over now.')
        print('You can finally go home.')
        print('The End...')
        print('')
        print('')
        print('')
        print('')
        print('')
        print('30 Years later...')
        print('Phone buzzes*')
        answer_phone = input('Pick up phone? (yes / no) ').lower()
        if answer_phone == 'yes':
            print(f'Hello? Is this {name}?')
            print(f'The one that lives at {address}?')
            print(f'The one with a best friend named {best_friend}?')
            print('Thank you just wanted to make sure you are the right person')
            print('...')
            print('...')
            print('...')
            print(f'You owe the bank {owe_to_bank}!')
            print('But since it has been 30 years, the amount you owe has been increased by 183%...')
            owe_to_bank = owe_to_bank * 183
            print(f'You now owe the bank {owe_to_bank}!')
            print('You better pay up within 5 - 10 business days.')
            print('Or else there will be trouble...')
            print('Call ends*')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('The True End...')
        elif answer_phone == 'no':
            print('That was weird...')
            print('Probably nothing anyways')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('Another 10 Years later...')
            print('Phone buzzes again*')
            print('...')
            print(f'Hello? Is this {name}?')
            print(f'The one that lives at {address}?')
            print(f'The one with a best friend named {best_friend}?')
            print('Thank you just wanted to make sure you are the right person')
            print('...')
            print('...')
            print('...')
            print(f'You owe the bank {owe_to_bank}!')
            print('But since it has been 40 years, the amount you owe has been increased by 246%...')
            owe_to_bank = owe_to_bank * 246
            print(f'You now owe the bank {owe_to_bank}!')
            print('You better pay up within 5 - 10 business days.')
            print('Or else there will be trouble...')
            print('Call ends*')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('The True End...')
        else:
            print(f'Hello? Is this {name}?')
            print(f'The one that lives at {address}?')
            print(f'The one with a best friend named {best_friend}?')
            print('Thank you just wanted to make sure you are the right person')
            print('...')
            print('...')
            print('...')
            print(f'You owe the bank {owe_to_bank}!')
            print('But since it has been 30 years, the amount you owe has been increased by 183%...')
            owe_to_bank = owe_to_bank * 183
            print(f'You now owe the bank {owe_to_bank}!')
            print('You better pay up within 5 - 10 business days.')
            print('Or else there will be trouble...')
            print('Call ends*')
            print('')
            print('')
            print('')
            print('')
            print('')
            print('The True End...')