import random
from Live import input_check


def generate_number(difficulty):
    return random.randint(0, difficulty)


def get_guess_from_user(difficulty):
    while True:
        user_input = int(input(f"Please enter your guess (It must be an integer between 1 and {difficulty}):"))
        if input_check(str(user_input), difficulty):
            break
        else:
            print("Invalid input")
    return user_input


def compare_results(to_guess, user_input):
    if to_guess == user_input:
        return True
    else:
        return False


def play(difficulty):
    user_input = get_guess_from_user(difficulty)
    secret_number = generate_number(difficulty)
    return compare_results(user_input, secret_number)
