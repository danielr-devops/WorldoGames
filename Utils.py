import subprocess
scores_file_name = 'Scores.txt'
BAD_RETURN_CODE = -1


def screen_cleaner():
    subprocess.run("cls", shell=True)
    return
