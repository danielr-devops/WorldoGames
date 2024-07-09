def input_check(user_input, expected_range):
    if user_input in [str(i) for i in range(1, expected_range + 1)]:
        return True
    else:
        return False


def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")
    return ""


def load_game():
    while True:
        game_number = input("""
        Please choose a game to play:
        1. Memory Game - a sequence of numbers will appear for 1 second and you have to
        guess it back
        2. Guess Game - guess a number and see if you chose like the computer
        3. Currency Roulette - try and guess the value of a random amount of USD in ILS
        """)
        if input_check(game_number, 3):
            break
        else:
            print("Invalid input")
    while True:
        game_difficulty = input("Please choose game difficulty from 1 to 5: ")
        if input_check(game_difficulty, 5):
            break
        else:
            print("Invalid input")
    return game_number, game_difficulty
