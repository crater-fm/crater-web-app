from rest_framework import serializers
from crater_api.models import Artist, Dj, Episode, Bookmark, Genre, Song, SongArtist

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['artist_id', 'artist_name']
        

class ArtistPlayCountSerializer(serializers.ModelSerializer):
    play_count = serializers.IntegerField()
    class Meta:
        model = Artist
        fields = ['artist_id', 'artist_name', 'play_count']
        
class DjDetails_ArtistPlayCountSerializer(serializers.ModelSerializer):
    djdetails_play_count = serializers.IntegerField()
    class Meta:
        model = Artist
        fields = ['artist_id', 'artist_name', 'djdetails_play_count']

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['song_id', 'song_name']

class SongArtistSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(many=False)
    song = SongSerializer(many=False)
    songartist_play_count = serializers.IntegerField()
    class Meta:
        model = SongArtist
        fields = ['song_artist_id', 'song', 'artist', 'songartist_play_count']
        
class DjSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dj
        fields = ['dj_id', 'dj_name', 'nts_artist_url']
        
class DjEpCountSerializer(serializers.ModelSerializer):
    episode_count = serializers.IntegerField()
    class Meta:
        model = Dj
        fields = ['dj_id', 'dj_name', 'nts_artist_url', 'episode_count']
        

class ArtistDetails_DjEpCountSerializer(serializers.ModelSerializer):
    artistdetails_episode_count = serializers.IntegerField()
    class Meta:
        model = Dj
        fields = ['dj_id', 'dj_name', 'nts_artist_url', 'artistdetails_episode_count']
        
class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ['episode_id', 'episode_name', 'episode_description', 'episode_date', 'episode_url', 'episode_platform']
        

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre_id', 'genre_name', 'genre_parent_string', 'parent_genre']
        
class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['bookmark_id', 'user']
        
class GlobalSearchSerializer(serializers.Serializer):
    artists = ArtistPlayCountSerializer(many=True)
    djs = DjEpCountSerializer(many=True)
    episodes = EpisodeSerializer(many=True)
    
class ArtistDetailsSerializer(serializers.Serializer):
    artist = ArtistSerializer(many=False)
    episodes = EpisodeSerializer(many=True)
    djs = ArtistDetails_DjEpCountSerializer(many=True)
    song_artists = SongArtistSerializer(many=True)
    

class DjDetailsSerializer(serializers.Serializer):
    dj = DjSerializer(many=False)
    episodes = EpisodeSerializer(many=True)
    artists = DjDetails_ArtistPlayCountSerializer(many=True)

class HomepageSummary(serializers.Serializer):
    artists = ArtistPlayCountSerializer(many=True)
    dj = DjSerializer(many=True)
    episodes = EpisodeSerializer(many=True)
