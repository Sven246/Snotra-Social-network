from app.core.models.channel_analytics import ChannelAnalytics
from sqlalchemy import func

class AnalyticsService:

    @staticmethod
    def get_post_views(post_id):
        return ChannelAnalytics.query.filter_by(post_id=post_id).count()

    @staticmethod
    def get_unique_viewers(post_id):
        return (
            ChannelAnalytics.query
            .filter_by(post_id=post_id)
            .with_entities(ChannelAnalytics.user_id)
            .distinct()
            .count()
        )

    @staticmethod
    def get_channel_views(channel_id):
        return ChannelAnalytics.query.filter_by(channel_id=channel_id).count()
