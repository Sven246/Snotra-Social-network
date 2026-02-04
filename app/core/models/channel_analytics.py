from app.extensions import db
from datetime import datetime

class ChannelAnalytics(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    channel_id = db.Column(db.Integer, db.ForeignKey("channel.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("channel_post.id"))

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    viewed_at = db.Column(db.DateTime, default=datetime.utcnow)

    # для удержания аудитории
    watch_time = db.Column(db.Integer, default=0)  # в секундах
