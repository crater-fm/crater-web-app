package org.crater.craterbackend;

import javax.persistence.*;

@Table(name = "episode")
@Entity
public class Episode {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "episode_id", nullable = false)
    private Integer id;

    @Lob
    @Column(name = "episode_name", nullable = false)
    private String episodeName;

    @Lob
    @Column(name = "episode_description")
    private String episodeDescription;

    @Lob
    @Column(name = "episode_date")
    private String episodeDate;

    @Lob
    @Column(name = "episode_url", nullable = false)
    private String episodeUrl;

    @Lob
    @Column(name = "episode_platform")
    private String episodePlatform;

    @ManyToOne
    @JoinColumn(name = "episode_dj_id")
    private EpisodeDj episodeDj;

    public EpisodeDj getEpisodeDj() {
        return episodeDj;
    }

    public void setEpisodeDj(EpisodeDj episodeDj) {
        this.episodeDj = episodeDj;
    }

    public String getEpisodePlatform() {
        return episodePlatform;
    }

    public void setEpisodePlatform(String episodePlatform) {
        this.episodePlatform = episodePlatform;
    }

    public String getEpisodeUrl() {
        return episodeUrl;
    }

    public void setEpisodeUrl(String episodeUrl) {
        this.episodeUrl = episodeUrl;
    }

    public String getEpisodeDate() {
        return episodeDate;
    }

    public void setEpisodeDate(String episodeDate) {
        this.episodeDate = episodeDate;
    }

    public String getEpisodeDescription() {
        return episodeDescription;
    }

    public void setEpisodeDescription(String episodeDescription) {
        this.episodeDescription = episodeDescription;
    }

    public String getEpisodeName() {
        return episodeName;
    }

    public void setEpisodeName(String episodeName) {
        this.episodeName = episodeName;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }
}