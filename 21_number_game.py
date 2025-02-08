## UNFINISHED. REASON: THE GAME IS TOOOO BORING! 

import sys

def check_consecutive_numbers(array_list):
    i = 1
    while i < len(array_list):
        if (array_list[i] - array_list[i-1]) == 1:
            print("All good! All Consecutive numbers")
            i += 1
        else:
            print("Inputed numbers are non-consecutive")
            return False
    return True 

def check_winner(array_list):
    if (array_list[-1])

 
def game_play(answer):
    number_list = []

    if answer == "F" or answer == "f":
        print("You have chosen to be Player 1")

        input_num = int(input("How many numbers do you want to enter? (max.3)"))
        if input_num <= 3:
            for i in range(input_num):
                new_num = int(input(f"Enter number {i + 1}: "))
                number_list.append(new_num)

            if check_consecutive_numbers(number_list):
                print(number_list)
            else:
                print("You Lost! Try Again.")
                print(number_list)
                sys.exit(0)

    elif answer == "S" or answer =="S":
        print("You have chosen to be Player 2")
    else:
        print("Invalid Input. Try Again")
        


def start_game():
    print("########################")
    print("#### 21 Number Game ####")
    print("########################")
    print()

    start_question = input("Do you want to start the game? y|n ")

    if start_question == "Y" or start_question == "y":
        print("Starting game....")
        print()
        flag = True 

        while flag == True: 
            first_or_second_question = input("Do you want to start First or Second? F|S ")
            game_play(first_or_second_question)

    elif start_question == "N" or start_question == "n":
        print("Ending program....")
        sys.exit(0)

    else:
        print("Invalid Input. Try Again")
        print()
    



# Main - Start game
start_game()