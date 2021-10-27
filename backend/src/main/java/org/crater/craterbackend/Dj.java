package org.crater.craterbackend;

import javax.persistence.*;

@Table(name = "dj")
@Entity
public class Dj {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "dj_id", nullable = false)
    private Integer id;

    @Lob
    @Column(name = "dj_name", nullable = false)
    private String djName;

    @Lob
    @Column(name = "nts_artist_url")
    private String ntsArtistUrl;

    public String getNtsArtistUrl() {
        return ntsArtistUrl;
    }

    public void setNtsArtistUrl(String ntsArtistUrl) {
        this.ntsArtistUrl = ntsArtistUrl;
    }

    public String getDjName() {
        return djName;
    }

    public void setDjName(String djName) {
        this.djName = djName;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }
}