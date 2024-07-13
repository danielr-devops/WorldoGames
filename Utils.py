import subprocess
SCORES_FILE_NAME = '/Scores.txt'
BAD_RETURN_CODE = -1


def screen_cleaner():
    subprocess.run("cls", shell=True)
    return

print("""
import freecurrencyapi


def get_money_interval(difficulty):
    client = freecurrencyapi.Client('fca_live_7BstNpTVgmzwMUAOBVLFLbCL6AizBxAbBLyOdiP1')
    result = client.latest()
    shekel = float(result['data']['ILS'])
    return (shekel - (5 - difficulty)), (shekel + (5 - difficulty))


def get_guess_from_user():
    return float(input("How much Israeli Shekels are in US Dollar, enter your guess: "))


def play(difficulty):
    user_guess = get_guess_from_user()
    boundaries = get_money_interval(difficulty)
    low_boundary = boundaries[0]
    high_boundary = boundaries[1]
    if user_guess < low_boundary or user_guess > high_boundary:
        return False
    else:
        return True

""")


screen_cleaner()