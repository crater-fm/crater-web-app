package org.crater.craterbackend;

import javax.persistence.*;

@Table(name = "setlist")
@Entity
public class Setlist {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "setlist_track_id", nullable = false)
    private Integer id;

    @ManyToOne(optional = false)
    @JoinColumn(name = "song_artist_id", nullable = false)
    private SongArtist songArtist;

    @ManyToOne(optional = false)
    @JoinColumn(name = "episode_id", nullable = false)
    private Episode episode;

    @Column(name = "setlist_seq", nullable = false)
    private Integer setlistSeq;

    public Integer getSetlistSeq() {
        return setlistSeq;
    }

    public void setSetlistSeq(Integer setlistSeq) {
        this.setlistSeq = setlistSeq;
    }

    public Episode getEpisode() {
        return episode;
    }

    public void setEpisode(Episode episode) {
        this.episode = episode;
    }

    public SongArtist getSongArtist() {
        return songArtist;
    }

    public void setSongArtist(SongArtist songArtist) {
        this.songArtist = songArtist;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }
}