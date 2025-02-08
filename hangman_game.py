import random
import sys

word_list = ["apple", "orange", "pineapple", "grape", "banana", "pear", "peach"]
selected_word = random.choice(word_list)
selected_word_length = len(selected_word)

# Game Controls
try_count = 0
max_try = selected_word_length + 2
guesses = ""

while try_count <= max_try:
    current_state = ""
    for char in selected_word:
        if char in guesses:
            print(char, end=" ")
            current_state += char
        else:
            print("_", end=" ")

    if current_state == selected_word:
        print("\nCongratulations! You won!")
        sys.exit(0)

    print("\n")
    if try_count > max_try:
        print(f"\nSorry, you've exceeded the maximum attempts. The correct word was: {selected_word}")
        sys.exit(0)

    guess = input("\nEnter a letter: ")
    guesses += guess
    try_count += 1
