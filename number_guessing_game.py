import math
import sys
import random

# get number range
try:
    min_num = int(input("Enter the minimum range: "))
    max_num = int(input("Enter the maximum range: "))

except ValueError:
    print("Wrong input. Please enter a whole number")
    sys.exit(1)

# get randum integer from within the range
def get_random_number(min_num, max_num):
    return random.randint(min_num, max_num)

random_number = get_random_number(min_num, max_num)

# Set minimum number of guesses
minimum_number_of_guesses = math.ceil(math.log(max_num - min_num + 1, 2))

# loop controls
guess_count = 0
flag = False # Flag variable is a control for the loop.

# Game loop
while flag is False:
    if guess_count <= minimum_number_of_guesses:
        try: 
            # get users guess
            users_guess = int(input(f"Guess the number between {min_num} and {max_num}: "))
        
        except ValueError:
            print("Wrong input. Please enter a whole number")
            sys.exit(1)

    
    
        if users_guess < random_number:
            print("Too low. Try again.")
            guess_count += 1
            print(f"\nYou have {minimum_number_of_guesses - guess_count} attempts left")

        elif users_guess > random_number:
            print("Too high. Try again.")
            guess_count += 1
            print(f"\nYou have {minimum_number_of_guesses - guess_count} attempts left")

        elif users_guess == random_number:
            guess_count += 1
            print(f"\nCongratulations! You guessed the number in {guess_count} attempts.")
            flag = True

    else:
        print("Game Over. You have exeeded the number of attempts")
        print(f"\nThe Random number is {random_number}")
        flag = True

        