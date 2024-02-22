# TOPIC 1: for loop vs. while loop
# for repetition in range(5):
#     print(f'Lifting weights repetition {repetition + 1} 🏋️‍♀️')
 
# repetition = 1
# while repetition <= 5:
#     print(f'WHILE: Lifting weights repetition {repetition} 🏋️‍♀️')
#     repetition += 1

# TODO: Write a program where the user has to guess a number chosen by the computer within the range of 1 to 100. The user will have a maximum of 10 attempts. After each guess, the program should indicate whether the guessed number is lower or higher than the chosen number.
# Task 1: Generate a random number.
# Task 2: Initialize a variable to keep track of the number of attempts.
# Task 3: Use a while loop to perform the following actions until the number is guessed or the number of attempts exceeds 10.
    # Task 3.1: Prompt the user to enter a number.
    # Task 3.2: Check the entered number and provide feedback ("too low", "too high", or "correct!").
    # Task 3.3: Increment the attempt counter.
# Task 4: If the user has not guessed the number, reveal the chosen number.

# TOPIC 2: break statement (breaking out of the loop)
# while True:
#     number = int(input("Enter a number (enter 0 to stop): "))
#     if number == 0:
#         print("0 detected, breaking the loop.")
#         break
#     else:
#         print(f"You entered {number}, continuing...")
# print("Loop terminated.")

# TODO: Find the secret number.
# Task 1: Repeatedly asks the user for numbers until the user enters a specific "secret" number (for example, 24). 
# Task 2: Once this number is entered, the program should print "Secret number found!" and terminate.
    
# # TOPIC 3: continue statement (skipping the rest of the code in the loop block and continuing with the next iteration)
# while True:
#     number = int(input("Enter a number (negative numbers will be ignored, enter 0 to stop): "))
#     if number == 0:
#         print("0 detected, breaking the loop.")
#         break
#     elif number < 0:
#         print("Negative number, continuing...")
#         continue
#     else:
#         print(f"You entered {number}")
# print("Loop terminated.")

# TODO: Skip even numbers.
# NOTE: The program should end when the user enters 0.
# Task 1: Ask the user to input numbers and prints only the odd numbers. 
# Task 2: If the user enters an even number, the program should skip it and proceed to the next input. 







