from app.extensions import db
from datetime import datetime

class ChannelPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    channel_id = db.Column(db.Integer, db.ForeignKey("channel.id"))
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    content = db.Column(db.Text, nullable=False)
    media_url = db.Column(db.String(255), nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    pinned = db.Column(db.Boolean, default=False)

    reactions = db.relationship("ChannelReaction", backref="post", lazy=True)
