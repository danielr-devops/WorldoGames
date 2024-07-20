from Utils import scores_file_name


def add_score(difficulty):
    point_of_wining = (difficulty * 3) + 5
    try:
        with open(scores_file_name, "r") as score_file:
            lines = score_file.readlines()
        prev_score = lines[-1].strip()
        lines[-1] = str(point_of_wining + int(prev_score)) + "\n"
        with open(scores_file_name, "w") as score_file:
            score_file.writelines(lines)
    except FileNotFoundError:
        with open(scores_file_name, "w") as score_file:
            score_file.write(str(point_of_wining) + "\n")
    except BaseException as e:
        print("Failed due to ", e.args)
