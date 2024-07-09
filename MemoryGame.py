import random
from time import sleep
from Live import input_check


def generate_sequence(difficulty):
    number_list = []
    for i in range(1, difficulty+1, 1):
        number_list.append(random.randint(0, 101))
    return number_list


def get_list_from_user(difficulty):
    users_number_list = []
    while True:
        if len(users_number_list) == difficulty:
            break
        user_input = int(input("Please enter a number you remembered :"))
        if input_check(str(user_input), 101):
            users_number_list.append(user_input)
            continue
        else:
            print("Invalid input")
    return users_number_list


def is_list_equal(user, computer):
    output = True
    for i in user:
        if i in computer:
            output = True
        else:
            output = False
    return output


def play(difficulty):
    print("The purpose of this game is to remember the numbers displayed,")
    print("A list of random numbers will be displayed for 0.7 seconds")
    print("If you were right about all the numbers you will win otherwise he will lose.")
    print("All guesses must be an integer between 1 and 101")
    print("Ready?\n\n")
    sleep(5)
    computer_sequence = generate_sequence(difficulty)
    print(computer_sequence, end='')
    sleep(0.7)
    print('\r', end='')
    user_sequence = get_list_from_user(difficulty)
    return is_list_equal(user_sequence, computer_sequence)
