package org.crater.craterbackend.model;

import javax.persistence.*;

@Table(name = "artist")
@Entity
public class Artist {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "artist_id", nullable = false)
    private Integer id;

    @Lob
    @Column(name = "artist_name", nullable = false)
    private String artistName;

    public String getArtistName() {
        return artistName;
    }

    public void setArtistName(String artistName) {
        this.artistName = artistName;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    @Override
    public String toString() {
        return "Artist [id=" + id + ", name=" + artistName + "]";
    }

}