import random
import sys

# get the name of the user
users_name = input("Please enter your name: ")
print(f"Welcome {users_name}")

# List of Words (Game will be focused on guessing the name of the footballer)
game_list = ["messi", "ronaldo", "mbappe", "haaland", "kaka", "ronaldinho", "henry", "neymar", "modric"]

# randon word selection
selected_word = random.choice(game_list)
selected_word_length = len(selected_word)
print("Random word selected...\n")

# game control
try_count = 0 # number of attempts
max_try = 12 # maximum number of of attempts
guesses = ""
flag = False # exit key

while (try_count <= max_try) or (flag == False):
    letter_count  = 0 # number of letters guessed correctly

    for letter in selected_word:
        if letter in guesses:
            letter_count += 1
            print(letter, end=" ")

        else:
            try_count += 1
            print("_", end=" ")

    print()

    if letter_count == selected_word_length:
        print(f"You Won! Congratulations {users_name}!!!\n")
        flag = True
        break
    
    # users alphabeth guess
    users_guess = input("\nGuess a letter in the selected word: ")
    guesses += users_guess

    