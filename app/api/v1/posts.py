from flask import request, jsonify
from flask_login import login_required, current_user
from app.extensions import db
from app.core.models.post import Post
from app.core.models.ad import Ad

def register(api):
    @api.route("/posts/create", methods=["POST"])
    @login_required
    def create_post():
        content = request.json.get("content")

        post = Post(
            user_id=current_user.id,
            content=content
        )
        db.session.add(post)
        db.session.commit()

        return jsonify({"status": "ok", "post_id": post.id})

    @api.route("/posts/feed")
    @login_required
    def feed():
        posts = Post.query.order_by(Post.created_at.desc()).limit(20).all()
        result = [
            {
                "id": p.id,
                "user_id": p.user_id,
                "content": p.content,
                "created_at": p.created_at.isoformat()
            }
            for p in posts
        ]

        # реклама
        if not current_user.is_premium:
            ad = Ad.query.filter_by(is_active=True).order_by(Ad.created_at.desc()).first()
            if ad:
                result.insert(2, {
                    "is_ad": True,
                    "title": ad.title,
                    "image_url": ad.image_url,
                    "link": ad.link
                })

        return jsonify(result)
