'''
Find episodes in which an artist was played
'''
SELECT
	artist.artist_id,
	artist.artist_name,
	episode.episode_id,
	episode.episode_name,
	episode.episode_date,
	episode.episode_url
FROM
	artist
INNER JOIN
	song_artist ON artist.artist_id = song_artist.artist_id
INNER JOIN 
	setlist ON song_artist.song_artist_id = setlist.song_artist_id
INNER JOIN
	episode ON setlist.episode_id = episode.episode_id
WHERE artist.artist_id = 1384
ORDER BY episode.episode_date DESC;

'''
Find DJs which played that artist
'''
SELECT
	artist.artist_id,
	artist.artist_name,
	count(dj.dj_id) as djcount,
	dj.dj_name
FROM
	artist
INNER JOIN
	song_artist ON artist.artist_id = song_artist.artist_id
INNER JOIN 
	setlist ON song_artist.song_artist_id = setlist.song_artist_id
INNER JOIN
	episode ON setlist.episode_id = episode.episode_id
INNER JOIN
	episode_dj ON episode.episode_id = episode_dj.episode_id
INNER JOIN
	dj ON episode_dj.dj_id = dj.dj_id
WHERE artist.artist_id = 1384
GROUP BY
	artist.artist_id,
	artist.artist_name,
	dj.dj_id
ORDER BY djcount DESC;

'''
Songs by the artist which were included in Setlists (ranked by play count, descending)
'''
SELECT
	setlist.song_artist_id,
	artist.artist_id,
	artist.artist_name,
	song.song_name,
	COUNT(setlist.song_artist_id) as song_artist_count
FROM
	setlist
INNER JOIN 
	song_artist ON setlist.song_artist_id = song_artist.song_artist_id
INNER JOIN
	artist ON song_artist.artist_id = artist.artist_id
INNER JOIN
	song ON song_artist.song_id = song.song_id
WHERE artist.artist_id = 1384
GROUP BY
	setlist.song_artist_id,
	artist.artist_id,
	artist.artist_name,
	song.song_name
ORDER BY song_artist_count DESC;
