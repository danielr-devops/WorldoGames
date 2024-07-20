import os
import subprocess
scores_file_name = 'Scores.txt'
BAD_RETURN_CODE = -1


def screen_cleaner():
    if os.name == 'posix':
        subprocess.run("clear", shell=True)
    else:
        subprocess.run("cls", shell=True)
    return
