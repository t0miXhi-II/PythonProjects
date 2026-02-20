import random

def main():
    target_score = 50
    number_of_players = get_number_of_players()

    scores = [ 0 for _ in range(number_of_players)]
    print(f"Scores: {scores}")

    while max(scores) < target_score:
        for i in range(number_of_players):
            print(f"Player {i + 1}")
            current_score = 0
            while True:
                attempt = input("Do you want to roll (y/n)?: ").lower()
                if attempt == 'y':
                    pass
                elif attempt == 'n':
                    break
                else:
                    print("Invalid input. Try again.")
                    continue
                
                player_roll = dice_roll()

                if player_roll != 1: 
                    current_score += player_roll
                else:
                    current_score = 0
                    #scores[i] = 0
                    break
                
                print()
                print(f"Scores: {scores}")
            
            scores[i] += current_score    
    
    print()
    print(f"Scores: {scores}")
    print(f"\n Game Over!!! Player {scores.index(max(scores)) + 1} wins!!!!!")





def dice_roll():
    max_value = 6
    min_value = 1
    attempt = random.randint(min_value, max_value)
    print(f"Dice Roll: {attempt}")
    return attempt


def get_number_of_players():
    while True:
        number_of_players = input("Enter number of players: ")
        if number_of_players.isdigit():
            number_of_players = int(number_of_players)
            break
        else:
            print("Invalid input. Try again.")
    return number_of_players


if __name__ == "__main__":
    main()