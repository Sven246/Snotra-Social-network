from flask import render_template
from flask_login import login_required, current_user

def register(web):

    @web.route("/")
    def index():
        return render_template("index.html")

    @web.route("/feed")
    @login_required
    def feed():
        return render_template("feed.html")

    @web.route("/profile")
    @login_required
    def profile():
        return render_template("profile.html", user=current_user)

    @web.route("/channels")
    @login_required
    def channels():
        return render_template("channels.html")
