from treasure_island import *

# TOPIC 1: Control flow with if/else and conditional operators (pictures #1, #2, #3)
# water_level = 50
# if water_level > 80:
#     print("Drain water")
# else:
#     print("Continue")

# TODO: Take a look at the given flow chart (picture #4). You have to program this using if/else statements.
# NOTE 1: If the height is higher than 120, log to the console: "You can ride the rollercoaster!"
# NOTE 2: In any other case, log to the console: "Sorry, you have to grow taller before you can ride."

# TOPIC 2: Modulo operator (remainder after a division)
# print(6 // 2)  # equals 3 (no remainder)
# print(6 % 2)  # (remainder 0)
# print(5 // 2)  # 2 * 2 + 1 (remainder 1)
# print(5 % 2)  # (remainder 1)
# print(14 // 4)  # 3 * 4 + 2 (remainder 2)
# print(14 % 4)  # (remainder 2)

# TODO: Write a program that works out whether if a given number is an odd or even number. 
# NOTE 1: If the number is even, log to the console: "This is an even number."
# NOTE 2: If the number is odd, log to the console: "This is an odd number."

# HINT: Even numbers can be divided by 2 with no remainder.

# TOPIC 3: Nested if statments (picture #5)
# meal = input('What meal are you planning to have? (breakfast/other): ')
# if meal == 'breakfast':
#    print('Suggested meal: Porridge with blueberries and mango.')
# else:
#    wish = input('What type of cuisine are you in the mood for? (asian/other): ')
#    if wish == 'asian':
#        print('Suggested meal: Ramen.')
#    else:
#        print('Suggested meal: Fish with mashed potatoes.')
    
# TODO: Take a look at the given flow chart (picture #6). You have to program this using nested if statements.
# NOTE 1: If the height is higher than 120, log to the console: "You can ride the rollercoaster!"
    # NOTE 1.1: If the age is equal or lower than 18, log to the console: "Please, pay $7."
    # NOTE 1.2: In any other case, log to the console: "Please, pay $12."
# NOTE 2: In any other case, log to the console: "Sorry, you have to grow taller before you can ride."

# TOPIC 4: elif (picture #7)
# meal = input('What meal are you planning? (breakfast/lunch/dinner/other): ')
# if meal == 'breakfast':
#    print('Suggested meal: Porridge with blueberries and mango.')
# elif meal == 'lunch':
#    print('Suggested meal: Chicken breast with couscous.')
# elif meal == 'dinner':
#    print('Suggested meal: Fish with mashed potatoes.')
# else:
#    print('Suggestion: Enjoy a milkshake!')

# TODO: Take a look at the given flow chart (picture #8). You have to program this using elif and nested if statements.
# NOTE 1: If the height is higher than 120, log to the console: "You can ride the rollercoaster!"
    # NOTE 1.1: If the age is lower than 12, log to the console: "Please, pay $5."
    # NOTE 1.2: If the age is equal or lower than 18, log to the console: "Please, pay $7."
    # NOTE 1.3: In any other case, log to the console: "Please, pay $12."
# NOTE 2: In any other case, log to the console: "Sorry, you have to grow taller before you can ride."

# TOPIC 5: match and case statements
# language = input("What's the programming language you want to learn? ")
# match language:
#     case "JavaScript":
#         print("You can become a web developer.")
#     case "Python":
#         print("You can become a Data Scientist")
#     case "Solidity":
#         print("You can become a Blockchain developer")
#     case _:
#         print("The language doesn't matter, what matters is solving problems.")

# TODO: Create your schedule for a week, using match and case statements.

# TOPIC 6: Multiple if statetements in succession (picture #9)
# weight = int(input('Please enter the weight of the cake in grams: '))
# taste = input('Please specify the filling flavor: ')
# if weight <= 3000:
#     price = 30
# else:
#     price = 50
# if taste == 'mango':
#     price += 7
# else:
#     price += 5
# print(f'The total price of the cake is: ${price}')

# TODO: Take a look at the given flow chart (picture #10). You have to program this using multiple if statetements.
# NOTE 1: If the height is higher than 120, log to the console: "You can ride the rollercoaster!"
    # NOTE 1.1: If the age is lower than 12, log to the console: "Please, pay $5."
    # NOTE 1.2: If the age is equal or lower than 18, log to the console: "Please, pay $7."
    # NOTE 1.3: In any other case, log to the console: "Please, pay $12."
    # NOTE 2.1: If people want a photo taken, add $3 to the bill. Log to the console: "The total bill is $_".
# NOTE 2: In any other case, log to the console: "Sorry, you have to grow taller before you can ride."

# TODO: Based on a user's order, work out their final bill.
# NOTE 1: Small pizza (S): $5; Medium pizza (M): $8; Large pizza (L): $12
# NOTE 2: Add pepperoni for small pizza (Y or N): +$2
# NOTE 3: Add pepperoni for medium or large pizza (Y or N): +$3
# NOTE 4: Add extra cheese for any size pizza (Y or N): +$1
# NOTE 5: Log to the console: "Your final bill is: $_."

# TOPIC 7: Logical operators (picture #11)
# allergic = input('Do you have any allergies? (yes/no): ')
# if allergic == 'yes':
#     allergy = input('What are you allergic to? ')
#     if allergy != 'milk' and allergy != 'gluten':
#         print('Offer cheesecakes.')

# TODO: Take a look at the given flow chart (picture #12). You have to program this using logical operators.
# NOTE 1: If the height is higher than 120, log to the console: "You can ride the rollercoaster!"
    # NOTE 1.1: If the age is lower than 12, log to the console: "Please, pay $5."
    # NOTE 1.2: If the age is between 12 and 18, log to the console: "Please, pay $7."
    # NOTE 1.3: If the age is equal or higher than 18, log to the console: "Please, pay $12."
    # NOTE 1.4: If the age is between 45 and 55, log to the console: "Have a free ride!"
    # NOTE 2.1: If people want a photo taken, add $3 to the bill.
# NOTE 2: In any other case, log to the console: "Sorry, you have to grow taller before you can ride."

# TODO: Take a look at the given flow chart and create a game "Treasure Island" (picture #13).
# print_game_logo()
# print_welcome_message()