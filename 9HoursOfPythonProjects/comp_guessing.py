# Computer Guessing Algo
"""
- grab number range from user
- select random number by user
- n/2 algorithm
- ramdom guess algo 
"""
import random as r
import statistics as s


def main():
    max_num = int(input("Enter Max number limit: "))
    min_num = int(input("Enter Min number limit: "))

    chosen_number = int(input(f"Enter a number between {min_num} and {max_num}: "))

    random_guess_algo(min_num, max_num, chosen_number)
    n_2_algo(min_num, max_num, chosen_number)
    #print(r.randint(min_num, max_num))
    #print((max_num - min_num) // 2)


def random_guess_algo(min_num: int, max_num: int, chosen_number: int):
    count = 0 

    while True:
        rComp_guess = r.randint(min_num, max_num)
        print(rComp_guess)
        
        if rComp_guess != chosen_number:
            count += 1
            if rComp_guess < chosen_number:
                #rComp_guess = r.randint(rComp_guess, max_num)
                min_num = rComp_guess
            else:
                #rComp_guess = r.randint(min_num, rComp_guess)
                max_num = rComp_guess
            print(count)
        else:
            print()
            print(f"Your number is {rComp_guess}")
            print(f"Random Guess Algo guessed the number in {count} attempt(s)!")
            break


def n_2_algo(min_num: int, max_num: int, chosen_number: int):
    count = 0 
    n2Comp_guess = 0

    while True:
        #n2Comp_guess = round((max_num - min_num) / 2)
        n2Comp_guess = round(s.median(range(min_num, max_num + 1)))
        print(n2Comp_guess)

        if n2Comp_guess != chosen_number:
            count += 1
            if n2Comp_guess < chosen_number:
                min_num = n2Comp_guess
            else: 
                max_num = n2Comp_guess
            print(count)
        else:
            print()
            print(f"Your number is {n2Comp_guess}")
            print(f"N/2 Algo guessed the number in {count} attempt(s)!")
            break


if __name__ == "__main__":
    main()

