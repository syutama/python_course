# TOPIC 1: Using the for loop with lists (picture #1)
# fruits = ['Apple', 'Peach', 'Pear']
# for fruit in fruits:
#     print(fruit)
#     print(fruit + 'Pie')
#     print(fruits)
# print(fruits)

# TODO: Write a program that calculates the average student height from a list of heights, using for loop.
# NOTE: Log to the console: "Number of students is _. Average height is _".

# HINT: The average height can be calculated by adding all the heights together and dividing by the total number of heights.

# TODO: Write a program that calculates the highest score from a list of scores, using for loop.
# NOTE: Log to the console: "The highest score in the class is: _".

# TOPIC 2: for loops and the range() function (pictures #2, #3, $4)
# for number in range(11):
#     print(number)

# for number in range(1, 11, 3):
#     print(number)

# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

# TODO: Write a program that calculates the sum of all the even numbers from 1 to X. 
# NOTE: If X is 100 then the first even number would be 2 and the last one is 100: 2 + 4 + 6 + ... + 98 + 100
# NOTE: The program should just print the final total, not every step of the calculation.

# TODO: Write a program that automatically prints the solution to the FizzBuzz game. 
# NOTE: Your program should print each number from 1 to 100 in turn and include number 100.
# Task 1: If the number is divisible by 3, then instead of printing the number it should print "Fizz".
# Task 2: If the number is divisible by 5, then instead of printing the number it should print "Buzz".
# Task 3: If the number is divisible by both 3 and 5, then instead of the number it should print "FizzBuzz".

# TODO (EASY LEVEL): Create the password generator (order of characters not randomised: e.g. 4 letter, 2 symbol, 2 number = JduE&!91)
# Task 1: Import the necessary module to work with random numbers.
# Task 2: Initialize a variable for the password as an empty string.
# Task 3: Using a loop, add random letters to the password in the quantity specified by the user.
# Task 4: Using a loop, add random symbols to the password in the quantity specified by the user.
# Task 5: Using a loop, add random numbers to the password in the quantity specified by the user.
# Task 6: Log to the console: "Your password is: _"

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the Python Password Generator!")
# num_letters= int(input("How many letters would you like in your password?\n")) 
# num_symbols = int(input("How many symbols would you like?\n"))
# num_numbers = int(input("How many numbers would you like?\n"))

# TODO (HARD LEVEL): Create the password generator (order of characters randomised: e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P)
# Task 1: Initialize an empty list to temporarily store password elements.
# Task 2: Using a loop, add random letters to the list in the quantity specified by the user.
# Task 3: Using a loop, add random symbols to the list in the quantity specified by the user.
# Task 4: Using a loop, add random numbers to the list in the quantity specified by the user.
# Task 5: Shuffle the elements of the list in random order.
# Task 6: Initialize an empty string for the final password.
# Task 7: Using a loop, convert the list of password elements into a string.
# Task 8: Log to the console: "Your password is: _"

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the Python Password Generator!")
# num_letters= int(input("How many letters would you like in your password?\n")) 
# num_symbols = int(input("How many symbols would you like?\n"))
# num_numbers = int(input("How many numbers would you like?\n"))