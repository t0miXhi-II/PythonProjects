import random

"""
#loop: cover computer and user response
#random: generate computer response
#get user response
compare responses
print winner
"""
def main():
    user_score = 0
    computer_score = 0
    count = 0
    while count <= 5:
        count += 1
        computer_response = random.choice(["rock", "paper", "scissors"])
        user_response = input("Enter option - Rock, Paper, or Scissors: ").lower()

        match user_response:
            case "rock":
                if computer_response == "rock":
                    print("It is a draw - Rock vs Rock")
                    print(f"Score: You - {user_score} || Computer - {computer_score}")
                elif computer_response == "paper":
                    print("Computer wins - Paper beats Rock")
                    computer_score += 1
                    print(f"Score: You - {user_score} || Computer - {computer_score}")
                elif computer_response == "scissors":
                    print("You win - Rock beats Scissors")
                    user_score += 1
                    print(f"Score: You - {user_score} || Computer - {computer_score}")
                else:
                    print("Opps. Something went wrong.")
                    continue
            case "paper":
                if computer_response == "paper":
                    print("It is a draw - Paper vs Paper")
                    print(f"Score: You - {user_score} || Computer - {computer_score}")
                elif computer_response == "rock":
                    print("You win - Paper beats Rock")
                    user_score += 1
                    print(f"Score: You - {user_score} || Computer - {computer_score}")
                elif computer_response == "scissors":
                    print("Computer wins - Scissors beats Paper")
                    computer_score += 1
                    print(f"Score: You - {user_score} || Computer - {computer_score}")
                else:
                    print("Opps. Something went wrong.")
                    continue
            case "scissors":
                if computer_response == "scissors":
                    print("It is a draw - Scissors vs Scissors")
                    print(f"Score: You - {user_score} || Computer - {computer_score}")
                elif computer_response == "paper":
                    print("You win - Scissors beats Paper")
                    user_score += 1
                    print(f"Score: You - {user_score} || Computer - {computer_score}")
                elif computer_response == "rock":
                    print("Computer wins - Rock beats Scissors")
                    computer_score += 1
                    print(f"Score: You - {user_score} || Computer - {computer_score}")
                else:
                    print("Opps. Something went wrong.")
                    continue
            case _:
                print("Invalid input. Try Again.")
                continue
        print()
    print()
    print(f"Final Score: You - {user_score} || Computer - {computer_score}")
    if user_score > computer_score:
        print("You win!!!")
    elif user_score < computer_score:
        print("Computer wins!!!")
    else:
        print("Its a draw!!!")
            

if __name__ == "__main__":
    main()