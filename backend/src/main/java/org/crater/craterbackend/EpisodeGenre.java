package org.crater.craterbackend;

import javax.persistence.*;

@Table(name = "episode_genre")
@Entity
public class EpisodeGenre {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "episode_genre_id", nullable = false)
    private Integer id;

    @ManyToOne(optional = false)
    @JoinColumn(name = "episode_id", nullable = false)
    private Episode episode;

    @ManyToOne(optional = false)
    @JoinColumn(name = "genre_id", nullable = false)
    private Genre genre;

    public Genre getGenre() {
        return genre;
    }

    public void setGenre(Genre genre) {
        this.genre = genre;
    }

    public Episode getEpisode() {
        return episode;
    }

    public void setEpisode(Episode episode) {
        this.episode = episode;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }
}