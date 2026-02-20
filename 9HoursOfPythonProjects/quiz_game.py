
def main():
    quiz = [
        {
            "question": "What is the meaning of CPU?",
            "answer": "Central Processing Unit"
        },
        {
            "question": "What is the meaning of RAM?",
            "answer": "Random Access Memory"
        },
        {
            "question": "What is the meaning of SSD",
            "answer": "Solid State Drive"
        },
        {
            "question": "What is the meaning of OS",
            "answer": "Operating System"
        }
    ]

    print("Welcome to my Quiz Game")

    playing = input("Do you want to play? y|n ")

    while True:
        match playing:
            case "y" | "Y":
                score = start_game(quiz)
                print(f"Quiz Completed. Final Score = {score}/{len(quiz)}")
                print()
                print("#################")
                break
            case "n" | "N":
                print("Thank you. Closing game now ....")
                break
            case _:
                print("Invalid Input. Try again.")



"""
desc: Function containing the game play
param: none
pType: none
return: user's score
rType: int
"""
def start_game(quiz):
    score = 0
    for quiz_item in quiz:
        print(quiz_item["question"])
        user_answer = input("Enter your answer: ")
        if user_answer.lower() == quiz_item["answer"].lower():
            score += 1
            print(f"Correct. Score: {score}")
        else:
            print("Incorrect...")
            print(f"Correct Answer: {quiz_item["answer"]}")
        
        print()
    return score


if __name__ == "__main__":
    main()