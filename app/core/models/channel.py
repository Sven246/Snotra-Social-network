from app.extensions import db
from datetime import datetime

class Channel(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)

    # публичный / приватный / премиум
    type = db.Column(db.String(50), default="public")

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # отключение рекламы за монеты
    ads_disabled = db.Column(db.Boolean, default=False)

    posts = db.relationship("ChannelPost", backref="channel", lazy=True)
    subscribers = db.relationship("ChannelSubscription", backref="channel", lazy=True)
