import random

Bible_books = [
    "Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy", "Joshua", "Judges", "Ruth", "Samuel", "Kings",
    "Chronicles", "Ezra", "Nehemiah", "Esther", "Job", "Psalms", "Proverbs", "Ecclesiastes", "Songs of Solomon", "Isaiah", 
    "Jeremiah", "Lamentations", "Ezekiel", "Daniel", "Hosea", "Joel", "Amos", "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk", 
    "Zephaniah", "Haggai", "Zechariah", "Malachi", "Matthew", "Mark", "Luke", "John", "Acts", "Romans", "Corinthians", "Galatians", 
    "Ephesians", "Philippians", "Colossians", "Thessalonians", "Timothy", "Titus", "Philemon", "Hebrews", "James", "Peter", "Jude", "Revelation"
]

MAX_ATTEMPTS = 10

def main():
    book_selection = random.choice(Bible_books).upper()
    attempts = 0

    print(randomise_name(book_selection).upper())
    print()

    while attempts <= MAX_ATTEMPTS:
        user_guess = input("Type in the correct book: ").upper().strip()

        if len(user_guess) > 0 :
            attempts += 1

            if user_guess == book_selection:
                print("Correct!!! You win!")
                break
            else:
                print("Incorrect. Try again.")
        else:
            print("No input was entered. Please try again.")


'''
Desc: Function for randomising the name of a Bible Book or any String
param: Name of Bible Book
pType: String
return: Randomised name of Bible Book
rType: String
'''
def randomise_name(name: str):
    chars = list(name)
    random.shuffle(chars)

    randomised_name = "".join(chars)

    return randomised_name



if __name__ == "__main__":
    main()