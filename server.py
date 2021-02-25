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


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
      <html>
        <head>
          <title> Hello! Click this link </title>
        </head>
        <body>
          <a href="/hello">Hello! Click this link for a compliment.</a> 
        <body>
      </html>
      """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
        </div>
          What's your name? <input type="text" name="person">
        </div>
        </div>
          <p>
            Select your compliment:
          <p>
          <p>
            <input type="radio" name="compliment" value="amazing">
            <label> Amazing </label>
            <input type="radio" name="compliment" value="awesome">
            <label> Awesome </label>
            <input type="radio" name="compliment" value="fabulous">
            <label> Fabulous </label>
            <p>
            <input type="submit" value="Submit">
            <p>
        </div>
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name and give a compliment."""

    player = request.args.get("person")
    
    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
