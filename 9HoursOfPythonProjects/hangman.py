import random
"""
create list of words
random word selection from list
grab user letter input
loop through word and compare input
"""
word_list = ['manchester', 'melbourne', 'paris', 'london', 'new york', 'boston', 'lagos', 'mardid', 'barcelona', 'milan']


def main():
    selected_word = random.choice(word_list)
    max_attempts = len(selected_word) + random.choice([2,3])
    attempts = 0

    guess_holder = ""
    
    
    while attempts <= max_attempts:
        user_guess = input("Enter a LETTER: ")
        correct_count = 0

        if len(user_guess) == 1:
            attempts += 1

            if user_guess in selected_word:
                if user_guess not in guess_holder:
                    guess_holder += user_guess

            else:
                print("Wrong guess, try again!")
                continue

        else:
            print("Invalid input. Please enter a SINGLE letter.")
            print()
            continue
    
        for each_letter in selected_word:
            if each_letter in guess_holder:
                print(each_letter, end=" ")
                correct_count += 1
            else:
                print("_", end=" ")

        if correct_count == len(selected_word):
            print()
            print("Congratulations!!!")
            break

        print()
    
    else:
        print(f"Game Over!!! The Selected word is {selected_word}.")

            
if __name__ == "__main__":
    main()