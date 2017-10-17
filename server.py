"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

DISSES = [
    "scurvey companion", "pigeon-liver'd hobby horse", "poisonous bunch-backed toad",
    "stewed prune", "bolting hutch of beastliness", "swollen parcel of dropsies",
    "huge bombard of sack", "stuffed cloak bag of guts", "plague sore"]


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html><html>Hi! This is the home page.
              <br>Let's go to the <a href="/hello">compliment page</a>!
    </html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""
    how_cool = ["somewhat cool", "super cool", "not that cool", "cool enough for the circumstances"]
    input_list = ""
    for compliment in how_cool:
        input_list = input_list + ('<input type="checkbox" name="compliment" value="{}">{}'
                                   .format(compliment, compliment.title()))

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/compliment"> <!-- asdgfasd-->
          What's your name? <input type="text" name="person"><br>
          What totally organic compliment would you like to give yourself?<br>
          {}
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """.format(input_list)


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    #getlist for list(checkbox), get for single argument(radio button)
    perceived_compliment = request.args.getlist("compliment")
    perceived_compliment = ", ".join(perceived_compliment) 

    compliment = choice(AWESOMENESS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! You think you're {coolness} ...<br>But I think you're {compliment}!
      </body>
    </html>
    """.format(player=player, coolness=perceived_compliment, compliment=compliment)


@app.route('/compliment')
def diss_person():
    """Diss misled user by name"""

    player = request.args.get("person")

    #getlist for list(checkbox), get for single argument(radio button)
    perceived_compliment = request.args.get("compliment")

    insult = choice(DISSES)

    return """
      <!doctype html>
      <html>
        <head>
          <title>A Compliment</title>
        </head>
        <body>
          Hi, {player}! You think you're {coolness} ...<br>But we think you're a {compliment}!
        </body>
      </html>
      """.format(player=player, coolness=perceived_compliment, compliment=insult)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
