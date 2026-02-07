from flask import request, jsonify
from flask_login import login_required, current_user
from app.core.services.channels_service import ChannelsService
from app.core.models.channel import Channel
from app.core.models.channel_post import ChannelPost
from app.core.models.ad import Ad

def register(api):
    @api.route("/channels/create", methods=["POST"])
    @login_required
    def create_channel():
        data = request.json
        channel = ChannelsService.create_channel(
            current_user,
            data.get("title"),
            data.get("description"),
            data.get("type")
        )
        return jsonify({"status": "ok", "channel_id": channel.id})

    @api.route("/channels/<int:channel_id>/posts")
    @login_required
    def get_posts(channel_id):
        posts = ChannelPost.query.filter_by(channel_id=channel_id).order_by(ChannelPost.created_at.desc()).all()

        result = [
            {
                "id": p.id,
                "content": p.content,
                "media_url": p.media_url,
                "created_at": p.created_at.isoformat()
            }
            for p in posts
        ]

        # реклама
        channel = Channel.query.get(channel_id)
        if not current_user.is_premium and not channel.ads_disabled:
            ad = Ad.query.filter_by(is_active=True, show_in_channels=True).first()
            if ad:
                result.insert(3, {
                    "is_ad": True,
                    "title": ad.title,
                    "image_url": ad.image_url,
                    "link": ad.link
                })

        return jsonify(result)
