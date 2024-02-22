from rock_paper_scissors import *

# TOPIC 1: Understanding the offset and appending items to lists
# fruits1 = []
# fruits2 = list()
# friends = ['Daniel', 'Polina']
# print(friends[0])
# print(friends[-1])
# friends[-1] = 'Kate'
# print(friends)
# friends.append('Victoria')
# print(friends)

# TOPIC 2: IndexErrors
# friends = ['Daniel', 'Kate', 'Victoria']
# print(len(friends))
# print(friends[2])
# print(friends[3])
# num_of_friends = len(friends)
# print(friends[num_of_friends])
# print(friends[num_of_friends - 1])

# TOPIC 3: split() method
# fruits = "apple, banana, pear"
# list_of_fruits = fruits.split(", ") 
# print("The words in the sentence are:", list_of_fruits)

# TODO: Create a list from the string.
# Task 1: Create a string animals with the following content: "dog, cat, parrot". 
# Task 2: Convert the animals string into a list named list_of_animals.
# Task 3: Print the message: "The animals in the list are: _".

# TOPIC 5: Import
# import random
# print(random.randint(2, 7))
# from random import randint
# print(randint(2, 7))
# from random import *
# print(randint(2, 7))

# TOPIC 6: Random module
# randomInteger = randint(3, 9)
# print(randomInteger)

# randomFloat1 = random()
# print(randomFloat1)
# randomFloat2 = random() * 10
# print(randomFloat2)

# fruits = ['apple', 'banana', 'pear']
# chosen_fruit = choice(fruits)
# print(f"The chosen fruit is: {chosen_fruit}")

# numbers = [1, 2, 3, 4, 5]
# shuffle(numbers)
# print(f"The shuffled numbers are: {numbers}")

# TODO: Write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
# Task 1: Generate a random number, either 0 or 1. 
# Task 2: For generated number print out "Heads" or "Tails".

# TODO: Write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
# Task 1: Request names.
# Task 2: Randomly choose one of the names.
# Task 3: Log to the console: "_ is going to buy the meal today!"

# HINT: Assume that names looks like this: 1 - input: name1, name2, name3; 2 - names = ["name1", "name2", "name3"].

# TOPIC 4: Working with nested lists
# dirty_dozen = ['Strawberries', 'Spinach', 'Kale', 'Nectarines', ' Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears', 'Tomatoes', 'Celery', 'Potatoes']
# dirty_dozen_fruits = ['Strawberries', 'Nectarines', ' Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears']
# dirty_dozen_vegetables = ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']
# dirty_dozen = [dirty_dozen_fruits, dirty_dozen_vegetables]
# print(dirty_dozen)
# print(dirty_dozen[0][3])

# TODO: Create a game "Rock Paper Scissors".
# Task 1: Import the random module.
# Task 2: Initialize the game_images list with the rock, paper, scissors variables.
# Task 3: Implement user choice logic.
# Task 4: Ensure the number is within the acceptable range. Otherwise, report an error.
# Task 5: Use the entered number to display the user's choice from the game_images list.
# Task 6: Generate the computer's choice.
# Task 7: Display the computer's choice.
# Task 8: Implement the logic to determine the winner based on the rules of "rock, paper, scissors".

# HINT 1: Use conditional operators to check the user's input for correctness. If a number outside the allowed range is entered, report an error.
# HINT 2: Remember that in the game "rock, paper, scissors," rock beats scissors, scissors beat paper, and paper beats rock.

