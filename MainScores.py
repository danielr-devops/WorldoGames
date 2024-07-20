from flask import Flask, request, render_template
from Utils import scores_file_name
app = Flask("ScoreServer")


def score_server(file_name):
    try:
        with open(file_name, "r") as score_file:
            score = score_file.readline()

            @app.route('/')
            def index():
                return render_template('score_template.html', SCORE=score)

            app.run(debug=True)
    except BaseException as e:
        print("Failed due to ", e.args[1])

        @app.route('/')
        def index():
            return render_template('error_template.html', ERROR=e.args[1])

        app.run(debug=True)
