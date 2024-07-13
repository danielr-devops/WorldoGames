from Live import load_game, welcome
from MemoryGame import play as memory_game_play
from GuessGame import play as guess_game_play
from CurrencyRouletteGame import play as currency_roulette_game_play
from Score import add_score
print(welcome(input("Please enter your name :")))
choice = load_game()
difficulty = int(choice[1])
match choice[0]:
    case "1":
        if memory_game_play(difficulty):
            print("You won!")
            add_score(difficulty)
        else:
            print("You lost...")
    case "2":
        if guess_game_play(difficulty):
            print("You won!")
            add_score(difficulty)
        else:
            print("You lost...")
    case "3":
        if currency_roulette_game_play(difficulty):
            print("You won!")
            add_score(difficulty)
        else:
            print("You lost...")
    case _:
        print("ERROR")
