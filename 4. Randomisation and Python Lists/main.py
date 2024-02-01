from rock_paper_scissors import *

# TOPIC 1: Import
# import random
# print(random.randint(2, 7))
# from random import randint
# print(randint(2, 7))
# from random import *
# print(randint(2, 7))

# TOPIC 2: Random module
# randomInteger = randint(3, 9)
# print(randomInteger)
# randomFloat1 = random()
# print(randomFloat1)
# randomFloat2 = random() * 5
# print(randomFloat2)

# TODO: Write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
# NOTE 1: Generate a random number, either 0 or 1. 
# NOTE 2: Then generated number to print out "Heads" or "Tails".

# TOPIC 3: Understanding the offset and appending items to lists
# friends = ['Daniel', 'Polina']
# print(friends[0])
# print(friends[-1])
# friends[-1] = 'Kate'
# print(friends)
# friends.append('Victoria')
    
# TODO: Write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
# NOTE 1: Line 32 splits the string names_string into individual names and puts them inside a list called names. 
# NOTE 2: There is need to be a space between the comma and the next name.
# NOTE 3: Log to the console: "_ is going to buy the meal today!"
# HINT: Assume that names looks like this: 1 - input: name1, name2, name3; 2 - names = ["name1", "name2", "name3"].
# names_string = input('')
# names = names_string.split(", ")

# TOPIC 4: IndexErrors
# friends = ['Daniel', 'Kate', 'Victoria']
# print(len(friends))
# print(friends[2])
# print(friends[3])
# num_of_friends = len(friends)
# print(friends[num_of_friends])
# print(friends[num_of_friends - 1])

# TOPIC 5: Working with nested lists
# dirty_dozen = ['Strawberries', 'Spinach', 'Kale', 'Nectarines', ' Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears', 'Tomatoes', 'Celery', 'Potatoes']
# dirty_dozen_fruits = ['Strawberries', 'Nectarines', ' Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears']
# dirty_dozen_vegetables = ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']
# dirty_dozen = [dirty_dozen_fruits, dirty_dozen_vegetables]
# print(dirty_dozen)
# print(dirty_dozen[0][3])

# TODO: Create a game "Rock Paper Scissors".
# Task 1: Import the random module.
# Task 2: Create rock, paper, scissors variables.
# Task 3: Initialize the game_images list with the rock, paper, scissors variables.
# Task 4: Implement user choice logic.
# Task 5: Ensure the number is within the acceptable range. Otherwise, report an error.
# Task 6: Use the entered number to display the user's choice from the game_images list.
# Task 7: Generate the computer's choice.
# Task 8: Display the computer's choice.
# Task 9: Implement the logic to determine the winner based on the rules of "rock, paper, scissors".

# HINT 1: Use conditional operators to check the user's input for correctness. If a number outside the allowed range is entered, report an error.
# HINT 2: Remember that in the game "rock, paper, scissors," rock beats scissors, scissors beat paper, and paper beats rock.
