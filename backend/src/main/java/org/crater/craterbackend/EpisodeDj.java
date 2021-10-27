package org.crater.craterbackend;

import javax.persistence.*;

@Table(name = "episode_dj")
@Entity
public class EpisodeDj {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "episode_dj_id", nullable = false)
    private Integer id;

    @ManyToOne(optional = false)
    @JoinColumn(name = "dj_id", nullable = false)
    private Dj dj;

    @ManyToOne(optional = false)
    @JoinColumn(name = "episode_id", nullable = false)
    private Episode episode;

    public Episode getEpisode() {
        return episode;
    }

    public void setEpisode(Episode episode) {
        this.episode = episode;
    }

    public Dj getDj() {
        return dj;
    }

    public void setDj(Dj dj) {
        this.dj = dj;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }
}