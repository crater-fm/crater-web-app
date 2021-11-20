from rest_framework import serializers
from crater_api.models import Artist, Dj, Episode, Bookmark

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['artist_id', 'artist_name']
        
class DjSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dj
        fields = ['dj_id', 'dj_name', 'nts_artist_url']
        
class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ['episode_id', 'episode_name', 'episode_description', 'episode_date', 'episode_url', 'episode_platform']
        
class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['bookmark_id', 'user']
        
class GlobalSearchSerializer(serializers.Serializer):
    artists = ArtistSerializer(many=True)
    djs = DjSerializer(many=True)
    episodes = EpisodeSerializer(many=True)
        
