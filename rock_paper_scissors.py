import random

def computersChoice(usersChoice):
    if usersChoice == 1:
        return random.choice([2,2])
    elif usersChoice == 2:
        return random.choice([1,3])
    elif usersChoice == 3:
        return random.choice([1,2])
    else:
        print("Invalid Input!")
        return False


def responseCheck(usersChoice, computersChoice):
    if (usersChoice == 1) and (computersChoice == 2):
        print("ROCK(you) vs PAPER(computer)")
        print("PAPER - Computer wins!")
    elif (usersChoice == 1) and (computersChoice == 3):
        print("ROCK(you) vs SCISSORS(computer)")
        print("ROCK - You win!")
    elif (usersChoice == 2) and (computersChoice == 1):
        print("PAPER(you) vs ROCK(computer)")
        print("PAPER - You win!")
    elif (usersChoice == 2) and (computersChoice == 3):
        print("PAPER(you) vs SCISSORS(computer)")
        print("SCISSORS - Computer wins!")
    elif (usersChoice == 3) and (computersChoice == 1):
        print("SCISSORS(you) vs ROCK(computer)")
        print("ROCK - Computer wins!")
    elif (usersChoice == 3) and (computersChoice == 2):
        print("SCISSORS(you) vs PAPER(computer)")
        print("SCISSORS - You win!")
    else:
        print("Invalid Input!")
        return False
    

def gamePlay():
    print("#################################")
    print("#### ROCK - PAPER - SCISSORS ####")
    print("#################################")
    print()

    gameState = True
    
    while gameState:
        print(" 1 - Rock")
        print(" 2 - Paper") 
        print(" 3 - Scissors")

        usersChoice = int(input("Enter your choice (1|2|3): "))
        computersDecision = computersChoice(usersChoice)
        responseCheck(usersChoice, computersDecision)

        playResponse = True

        while playResponse:
            playAgain = input("Do you want to play again? y|n : ")

            if playAgain.capitalize() == "Y":
                playResponse = False
                print()
                print("Get Ready....")
                print()
                break
            elif playAgain.capitalize() == "N":
                playResponse = False
                gameState = False 
                print()
                print("Ending game.....")
                break
            else: 
                print("Invaid Response! Try Again")
                print()


gamePlay()
