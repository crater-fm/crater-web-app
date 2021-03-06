# Generated by Django 3.2.9 on 2021-11-17 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('artist_id', models.AutoField(primary_key=True, serialize=False)),
                ('artist_name', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'artist',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('bookmark_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
            ],
            options={
                'db_table': 'bookmark',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CraterUsers',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_email', models.TextField(unique=True)),
                ('token', models.TextField(blank=True, null=True)),
                ('password_digest', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'crater_users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dj',
            fields=[
                ('dj_id', models.AutoField(primary_key=True, serialize=False)),
                ('dj_name', models.TextField(unique=True)),
                ('nts_artist_url', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dj',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('episode_id', models.AutoField(primary_key=True, serialize=False)),
                ('episode_name', models.TextField()),
                ('episode_description', models.TextField(blank=True, null=True)),
                ('episode_date', models.TextField(blank=True, null=True)),
                ('episode_url', models.TextField(unique=True)),
                ('episode_platform', models.TextField()),
            ],
            options={
                'db_table': 'episode',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EpisodeDj',
            fields=[
                ('episode_dj_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'episode_dj',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EpisodeGenre',
            fields=[
                ('episode_genre_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'episode_genre',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('genre_id', models.AutoField(primary_key=True, serialize=False)),
                ('genre_name', models.TextField(unique=True)),
                ('genre_parent_string', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'genre',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ParentGenre',
            fields=[
                ('parent_genre_id', models.AutoField(primary_key=True, serialize=False)),
                ('parent_genre_name', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'parent_genre',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Setlist',
            fields=[
                ('setlist_track_id', models.AutoField(primary_key=True, serialize=False)),
                ('setlist_seq', models.IntegerField()),
            ],
            options={
                'db_table': 'setlist',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('song_id', models.AutoField(primary_key=True, serialize=False)),
                ('song_name', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'song',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SongArtist',
            fields=[
                ('song_artist_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'song_artist',
                'managed': False,
            },
        ),
    ]
