from flask import jsonify
from flask_login import login_required
from app.core.services.analytics_service import AnalyticsService

def register(api):
    @api.route("/analytics/post/<int:post_id>")
    @login_required
    def post_stats(post_id):
        return jsonify({
            "views": AnalyticsService.get_post_views(post_id),
            "unique": AnalyticsService.get_unique_viewers(post_id)
        })
