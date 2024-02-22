from treasure_island import *

# TOPIC 1: Control flow with if/else and conditional operators (pictures #1, #2, #3)
# water_level = 50
# if water_level > 80:
#     print("Drain water")
# else:
#     print("Continue")

# TODO: Take a look at the given flow chart (picture #4). You have to program this using if/else statements.
# Task 1: Request the user's height.
# Task 2: If the height is greater than 120cm, log to the console: "You can ride the rollercoaster!"
# Task 3: In any other case, log to the console: "Sorry, you have to grow taller before you can ride."

# TOPIC 2: Modulo operator (remainder after a division)
# print(6 // 2)  # equals 3 (no remainder)
# print(6 % 2)  # (remainder 0)
# print(5 // 2)  # 2 * 2 + 1 (remainder 1)
# print(5 % 2)  # (remainder 1)
# print(14 // 4)  # 3 * 4 + 2 (remainder 2)
# print(14 % 4)  # (remainder 2)

# TODO: Write a program that works out whether if a given number is an odd or even number. 
# Task 1: If the number is even, log to the console: "This is an even number."
# Task 2: If the number is odd, log to the console: "This is an odd number."

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
# Task 1: Request the user's height.
# Task 2: If the height is greater than 120cm, log to the console: "You can ride the rollercoaster!"
    # Task 2.1: Request the user's age to determine the ticket price.
    # Task 2.2: If the user is 18 or under years old, log to the console: "Please, pay $7."
    # Task 2.3: In any other case, log to the console: "Please, pay $12."
# Task 3: In any other case, log to the console: "Sorry, you have to grow taller before you can ride."

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
# Task 1: Request the user's height.
# Task 2: If the height is greater than 120cm, log to the console: "You can ride the rollercoaster!"
    # Task 2.1: Request the user's age to determine the ticket price.
    # Task 2.2: If the user is under 12 years old, log to the console: "Please, pay $5."
    # Task 2.3: If the user is between 12 and 18 years old, log to the console: "Please, pay $7."
    # Task 2.4: If the user is older than 18, log to the console: "Please, pay $12."
# Task 3: In any other case, log to the console: "Sorry, you have to grow taller before you can ride."
    
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
# Task 1: Request the user's height.
# Task 2: If the height is greater than 120cm, log to the console: "You can ride the rollercoaster!"
    # Task 2.1: Request the user's age to determine the ticket price.
    # Task 2.2: If the user is under 12 years old, set the price to $5.
    # Task 2.3: If the user is between 12 and 18 years old, set the price to $7.
    # Task 2.4: If the user is older than 18, set the price to $12.
    # Task 3: Ask the user if they want a photo taken and add the cost to the ticket price.
        # Task 3.1: If the user wants a photo, add $3 to the ticket price.
    # Task 4: Log to the console: "The total bill is $_".
# Task 5: In any other case, log to the console: "Sorry, you have to grow taller before you can ride."

# TODO: Based on a user's order, work out their final bill.
# Task 1: Small pizza (S): $5; Medium pizza (M): $8; Large pizza (L): $12
# Task 2: Add pepperoni for small pizza (Y or N): +$2
# Task 3: Add pepperoni for medium or large pizza (Y or N): +$3
# Task 4: Add extra cheese for any size pizza (Y or N): +$1
# Task 5: Log to the console: "Your final bill is: $_."

# TOPIC 7: Logical operators (picture #11)
# allergic = input('Do you have any allergies? (yes/no): ')
# if allergic == 'yes':
#     allergy = input('What are you allergic to? ')
#     if allergy != 'milk' and allergy != 'gluten':
#         print('Offer cheesecakes.')

# TODO: Take a look at the given flow chart (picture #12). You have to program this using logical operators.
# Task 1: Request the user's height.
# Task 2: If the height is greater than 120cm, log to the console: "You can ride the rollercoaster!"
    # Task 2.1: Request the user's age to determine the ticket price.
    # Task 2.2: If the user is under 12 years old, set the price to $5.
    # Task 2.3: If the user is between 12 and 18 years old, set the price to $7.
    # Task 2.4: If the user is older than 18, set the price to $12.
    # Task 2.5: If the user is aged between 45 and 60, they ride for free.
    # Task 3: Ask the user if they want a photo taken and add the cost to the ticket price.
        # Task 3.1: If the user wants a photo, add $3 to the ticket price.
    # Task 4: Log to the console: "The total bill is $_".
# Task 5: In any other case, log to the console: "Sorry, you have to grow taller before you can ride."

# TODO: Take a look at the given flow chart and create a game "Treasure Island" (picture #13).
# print_game_logo()
# print_welcome_message()

                  

        