# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Artist(models.Model):
    artist_id = models.AutoField(primary_key=True)
    artist_name = models.TextField(unique=True)

    def __str__(self):
        return self.artist_name
    
    class Meta:
        db_table = 'artist'


class CraterUsers(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_email = models.TextField(unique=True)
    token = models.TextField(blank=True, null=True)
    password_digest = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.user_email

    class Meta:
        db_table = 'crater_users'


class Dj(models.Model):
    dj_id = models.AutoField(primary_key=True)
    dj_name = models.TextField(unique=True)
    nts_artist_url = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.dj_name

    class Meta:
        db_table = 'dj'


class Episode(models.Model):
    episode_id = models.AutoField(primary_key=True)
    episode_name = models.TextField()
    episode_description = models.TextField(blank=True, null=True)
    episode_date = models.TextField(blank=True, null=True)
    episode_url = models.TextField(unique=True)
    episode_platform = models.TextField()
    
    def __str__(self):
        return self.episode_name

    class Meta:
        db_table = 'episode'


class EpisodeDj(models.Model):
    episode_dj_id = models.AutoField(primary_key=True)
    dj = models.ForeignKey(Dj, models.DO_NOTHING)
    episode = models.ForeignKey(Episode, models.DO_NOTHING)
    
    def __str__(self):
        return self.episode_dj_id

    class Meta:
        db_table = 'episode_dj'
        unique_together = (('dj', 'episode'),)


class EpisodeGenre(models.Model):
    episode_genre_id = models.AutoField(primary_key=True)
    episode = models.ForeignKey(Episode, models.DO_NOTHING)
    genre = models.ForeignKey('Genre', models.DO_NOTHING)
    
    def __str__(self):
        return self.episode_genre_id

    class Meta:
        db_table = 'episode_genre'
        unique_together = (('episode', 'genre'),)


class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    genre_name = models.TextField(unique=True)
    genre_parent_string = models.TextField(blank=True, null=True)
    parent_genre = models.ForeignKey('ParentGenre', models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.genre_name

    class Meta:
        managed = False
        db_table = 'genre'


class ParentGenre(models.Model):
    parent_genre_id = models.AutoField(primary_key=True)
    parent_genre_name = models.TextField(unique=True)
    
    def __str__(self):
        return self.parent_genre_name

    class Meta:
        db_table = 'parent_genre'


class Setlist(models.Model):
    setlist_track_id = models.AutoField(primary_key=True)
    song_artist = models.ForeignKey('SongArtist', models.DO_NOTHING)
    episode = models.ForeignKey(Episode, models.DO_NOTHING)
    setlist_seq = models.IntegerField()
    
    def __str__(self):
        return self.setlist_track_id

    class Meta:
        db_table = 'setlist'
        unique_together = (('song_artist', 'episode', 'setlist_seq'),)


class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    song_name = models.TextField(unique=True)
    
    def __str__(self):
        return self.song_name

    class Meta:
        db_table = 'song'


class SongArtist(models.Model):
    song_artist_id = models.AutoField(primary_key=True)
    song = models.ForeignKey(Song, models.DO_NOTHING)
    artist = models.ForeignKey(Artist, models.DO_NOTHING)
    
    def __str__(self):
        return self.song_artist_id

    class Meta:
        db_table = 'song_artist'
        unique_together = (('song', 'artist'),)
        
class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

class Bookmark (models.Model):
    bookmark_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    
    class Meta:
        db_table = 'bookmark'
        unique_together = (('bookmark_id', 'user'),)
    

