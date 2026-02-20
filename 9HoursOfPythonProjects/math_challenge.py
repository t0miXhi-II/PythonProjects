import random

def main():
    MAX_RANGE = 20
    MIN_RANGE = 2
    OPERANDS = ["+", "-", "*"]

    first_var = random.randint(MIN_RANGE, MAX_RANGE)
    second_var = random.randint(MIN_RANGE, MAX_RANGE)

    operation = random.choice(OPERANDS)
    quiz = str(first_var) + operation + str(second_var)
    result = eval(quiz)

    print(f"{quiz} = {result}")


if __name__ == "__main__":
    main()