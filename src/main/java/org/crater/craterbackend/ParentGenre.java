package org.crater.craterbackend;

import javax.persistence.*;

@Table(name = "parent_genre")
@Entity
public class ParentGenre {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "parent_genre_id", nullable = false)
    private Integer id;

    @Lob
    @Column(name = "parent_genre_name", nullable = false)
    private String parentGenreName;

    public String getParentGenreName() {
        return parentGenreName;
    }

    public void setParentGenreName(String parentGenreName) {
        this.parentGenreName = parentGenreName;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }
}