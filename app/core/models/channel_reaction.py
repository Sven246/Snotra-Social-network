from app.extensions import db
from datetime import datetime

class ChannelReaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    post_id = db.Column(db.Integer, db.ForeignKey("channel_post.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    emoji = db.Column(db.String(10), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
