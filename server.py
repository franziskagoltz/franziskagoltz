"""Personal Website"""


from flask import Flask, render_template, redirect, request, flash, session
from jinja2 import StrictUndefined


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True


@app.route("/")
def index():
    """Shows landing page"""

    return render_template("homepage.html")


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    # app.debug = False

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run()
