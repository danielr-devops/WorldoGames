from Utils import scores_file_name


def add_score(difficulty):
    point_of_wining = (difficulty * 3) + 5
    try:
        with open(scores_file_name, "a") as score_file:
            score_file.write(str(point_of_wining))
    except IOError:
        print("IO Error")
    except BaseException as e:
        print("Failed due to ", e.args)


add_score(3)
