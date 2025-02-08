import random
import sys

unknown_number = random.randrange(1000,10000)
user_guess = input("Guess the 4 digit nummber: ")

# Number-to-String conversions
str_unknown_number = str(unknown_number)
str_user_guess = str(user_guess)

current_state = ["X"] * len(str_unknown_number)
game_flag = False
    
if user_guess == unknown_number:
    print("Congratulations!!! You won!")
    print("You are a Mastermind")

else:        
    while game_flag == False:
        count = 0 # Count the numbers correctly guessed
        print("wrong number, try again.")
            
        for i in range(0, len(str_unknown_number)):
            if str_user_guess[i] == str_unknown_number[i]:
                current_state[i] = str_unknown_number[i]

                if current_state[i] == str_unknown_number[i]:
                    count += 1

                print("Count: ", count)

        print(f"/n{current_state}")

        if count == 4:
            print("Congratulations!!! You won!")
            game_flag = True
            sys.exit(0)

        user_guess = input("\nGuess the 4 digit nummber: ")
        str_user_guess = str(user_guess)
