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
    play_count = models.IntegerField()
    songs = models.ManyToManyField('Song', through='SongArtist')

    class Meta:
        managed = False
        db_table = 'artist'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


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


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CraterUsers(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_email = models.TextField(unique=True)
    token = models.TextField(blank=True, null=True)
    password_digest = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crater_users'


class Dj(models.Model):
    dj_id = models.AutoField(primary_key=True)
    dj_name = models.TextField(unique=True)
    nts_artist_url = models.TextField(blank=True, null=True)
    episode_count = models.IntegerField()
    episodes = models.ManyToManyField('Episode', through='EpisodeDj')

    class Meta:
        managed = False
        db_table = 'dj'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Episode(models.Model):
    episode_id = models.AutoField(primary_key=True)
    episode_name = models.TextField()
    episode_description = models.TextField(blank=True, null=True)
    episode_date = models.TextField(blank=True, null=True)
    episode_url = models.TextField(unique=True)
    episode_platform = models.TextField()
    genres = models.ManyToManyField('Genre',through='EpisodeGenre')
    song_artists = models.ManyToManyField('SongArtist', through='Setlist')

    class Meta:
        managed = False
        db_table = 'episode'


class EpisodeDj(models.Model):
    episode_dj_id = models.AutoField(primary_key=True)
    dj = models.ForeignKey(Dj, models.DO_NOTHING)
    episode = models.ForeignKey(Episode, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'episode_dj'
        unique_together = (('dj', 'episode'),)


class EpisodeGenre(models.Model):
    episode_genre_id = models.AutoField(primary_key=True)
    episode = models.ForeignKey(Episode, models.DO_NOTHING)
    genre = models.ForeignKey('Genre', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'episode_genre'
        unique_together = (('episode', 'genre'),)


class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    genre_name = models.TextField(unique=True)
    genre_parent_string = models.TextField(blank=True, null=True)
    parent_genre = models.ForeignKey('ParentGenre', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genre'


class ParentGenre(models.Model):
    parent_genre_id = models.AutoField(primary_key=True)
    parent_genre_name = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'parent_genre'


class Setlist(models.Model):
    setlist_track_id = models.AutoField(primary_key=True)
    song_artist = models.ForeignKey('SongArtist', models.DO_NOTHING)
    episode = models.ForeignKey(Episode, models.DO_NOTHING)
    setlist_seq = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'setlist'
        unique_together = (('song_artist', 'episode', 'setlist_seq'),)


class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    song_name = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'song'


class SongArtist(models.Model):
    song_artist_id = models.AutoField(primary_key=True)
    song = models.ForeignKey(Song, models.DO_NOTHING)
    artist = models.ForeignKey(Artist, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'song_artist'
        unique_together = (('song', 'artist'),)
        

class Bookmark(models.Model):
    bookmark_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    artist = models.ForeignKey(
        Artist, models.DO_NOTHING, blank=True, null=True)
    dj = models.ForeignKey('Dj', models.DO_NOTHING, blank=True, null=True)
    episode = models.ForeignKey(
        'Episode', models.DO_NOTHING, blank=True, null=True)
    song_artist = models.ForeignKey(
        'SongArtist', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bookmark'
