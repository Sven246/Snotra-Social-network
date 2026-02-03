from app.extensions import db
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    # Premium
    is_premium = db.Column(db.Boolean, default=False)
    premium_expires_at = db.Column(db.DateTime, nullable=True)
    is_verified = db.Column(db.Boolean, default=False)

    # Coins
    coins_balance = db.Column(db.Integer, default=300)

    # UI settings
    theme = db.Column(db.String(50), default="default")
    hide_online = db.Column(db.Boolean, default=False)
    profile_background = db.Column(db.String(255), nullable=True)

    # Relations
    posts = db.relationship("Post", backref="author", lazy=True)
    comments = db.relationship("Comment", backref="author", lazy=True)
    stories = db.relationship("Story", backref="author", lazy=True)
