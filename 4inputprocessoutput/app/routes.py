from flask import Blueprint, render_template, request

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def home():

    message = ""

    if request.method == "POST":

        username = request.form.get("username")
        username1 = request.form.get("username1")

        message = f"Hello {username}, Welcome to Flask!"
        message1 = f"Hello {username1}, Welcome to Flask!"

    return render_template(
        "index.html",
        message=message,message1=message1
    )