from rest_framework import serializers

from movielist.models import Watchlist, StreamPlatform


class WatchlistSerializer(serializers.ModelSerializer):
    """Add a custom field. this field is not in the Movie model"""

    class Meta:
        model = Watchlist
        fields = '__all__'


class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    watchlist = WatchlistSerializer(many=True, read_only=True)
    # url = serializers.HyperlinkedIdentityField(view_name="watchlist:stream-detail")
    # watchlist = serializers.StringRelatedField(many=True)
    # watchlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='movie-detail')

    class Meta:
        model = StreamPlatform
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'watchlist:stream-detail'},
        }
