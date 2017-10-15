"""
webserver.py

File that is the central location of code for your webserver.
"""

from flask import Flask, render_template, request	
import os
import requests

# Create application, and point static path (where static resources like images, css, and js files are stored) to the
# "static folder"
app = Flask(__name__,static_url_path="/static")

@app.route("/")
def hello_world():
    """
    If someone goes to the root of your website (i.e. http://localhost:5000/), run this function. The string that this
    returns will be sent to the browser
    """
    return render_template("index.html") # Render the template located in "templates/index.html"

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/blog/8-experiments-in-motivation")
def blog1():
	return render_template("blog1.html")

@app.route("/blog/a-mindful-shift-of-focus")
def blog2():
	return render_template("blog2.html")

@app.route("/blog/how-to-develop-an-awesome-sense-of-direction")
def blog3():
	return render_template("blog3.html")

@app.route("/blog/training-to-be-a-good-writer")
def blog4():
	return render_template("blog4.html")

@app.route("/blog/what-productivity-systems-wont-solve")
def blog5():
	return render_template("blog5.html")


@app.route("/contact", methods=["GET"])
def contact():
	return render_template("contact.html", notifications=[])	

@app.route("/contact", methods=["POST"])
def send_email():
	message = request.form.get("message")
	notifications = []
	subject = request.form.get("subject")
	messagesent = "Hi " + request.form.get("firstname") + " Your Email Was Sent!"
	data = {
	    "from": os.environ["INFO253_MAILGUN_FROM_EMAIL"],
        "to": os.environ["INFO253_MAILGUN_TO_EMAIL"],
	    "subject": subject,
	    "text": message,
	}
	auth = ("api", os.environ["INFO253_MAILGUN_PASSWORD"])
	r = requests.post("https://api.mailgun.net/v3/{}/messages".format(os.environ["INFO253_MAILGUN_DOMAIN"]), auth=auth, data=data)
	if r.status_code == requests.codes.ok:
		notifications.append(messagesent)
	else:
		notifications.append("You're email was not sent. Please try again later.")
	return render_template("contact.html", notifications=notifications)

if __name__ == "__main__":
	app.run()
