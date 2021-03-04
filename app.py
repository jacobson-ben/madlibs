from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route("/questions")
def get_questions():

    keys = silly_story.prompts
    text = silly_story.template

    return render_template(
        "questions.html",
        keys=keys,
        text=text)
