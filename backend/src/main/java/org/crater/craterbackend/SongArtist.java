package org.crater.craterbackend;

import org.crater.craterbackend.model.Artist;

import javax.persistence.*;

@Table(name = "song_artist")
@Entity
public class SongArtist {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "song_artist_id", nullable = false)
    private Integer id;

    @ManyToOne(optional = false)
    @JoinColumn(name = "song_id", nullable = false)
    private Song song;

    @ManyToOne(optional = false)
    @JoinColumn(name = "artist_id", nullable = false)
    private Artist artist;

    public Artist getArtist() {
        return artist;
    }

    public void setArtist(Artist artist) {
        this.artist = artist;
    }

    public Song getSong() {
        return song;
    }

    public void setSong(Song song) {
        this.song = song;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }
}