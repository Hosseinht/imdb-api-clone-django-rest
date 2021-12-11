from rest_framework import serializers

from movielist.models import Watchlist, StreamPlatform


class WatchlistSerializer(serializers.ModelSerializer):
    """Add a custom field. this field is not in the Movie model"""

    class Meta:
        model = Watchlist
        fields = '__all__'


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchlistSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = '__all__'
