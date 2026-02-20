import random

""""
desc: Guess the correct number from within a range
"""
def main():
    start_game()


"""
desc: Game play function
param: none
return: none
"""
def start_game():
    score = 0
    top_limit = get_integer(input("Enter upper range value: "))
    bottom_limit = get_integer(input("Enter the bottom limit: "))
    number_of_guesses = (top_limit - bottom_limit) // 2
    
    print(f"You have {number_of_guesses} attempts")
    selected_number = random.randint(bottom_limit, top_limit)

    while True:
        user_input = input(f"Guess the number between {top_limit} and {bottom_limit}: ")

        if user_input.isdigit():
            user_input = int(user_input)
            # if user input range is valid ...
            if (bottom_limit <= user_input) and (top_limit >= user_input):
                if user_input == selected_number:
                    score = number_of_guesses
                    print(f"You won!!! Your score is {score}")
                    break
                elif user_input < selected_number:
                    print("Too low...")
                elif user_input > selected_number:
                    print("Too high...")
                else:
                    print("Invalid Input")
                
                number_of_guesses -= 1

                if number_of_guesses <= 0:
                    print("Game Over")
                    print(f"The selected number is {selected_number}")
                print()

            else:
                print("Invalid Input")
                print(f"Select a number within the range {bottom_limit} - {top_limit}")

        else:
            print("Invalid input. Number input is required.")
        print()




"""
desc: Integer input validation (for guessing range)
param: string input
pType: str
return: integer number
rType: int
"""
def get_integer(user_input: str):
    while True: 
        if user_input.isdigit():
            print("Input Confirmed.")
            return int(user_input)
        elif user_input=="1111":
            print("Exit code entered! Function terminated.")
        else:
            print("Invalid Input")
            user_input = input("Please enter a valid number: ")


if __name__ == "__main__":
    main()