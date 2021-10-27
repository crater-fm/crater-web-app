package org.crater.craterbackend;

import javax.persistence.*;
import java.time.Instant;

@Table(name = "crater_users")
@Entity
public class CraterUser {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "user_id", nullable = false)
    private Integer id;

    @Lob
    @Column(name = "user_email", nullable = false)
    private String userEmail;

    @Lob
    @Column(name = "token")
    private String token;

    @Lob
    @Column(name = "password_digest")
    private String passwordDigest;

    @Column(name = "created_at")
    private Instant createdAt;

    public Instant getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(Instant createdAt) {
        this.createdAt = createdAt;
    }

    public String getPasswordDigest() {
        return passwordDigest;
    }

    public void setPasswordDigest(String passwordDigest) {
        this.passwordDigest = passwordDigest;
    }

    public String getToken() {
        return token;
    }

    public void setToken(String token) {
        this.token = token;
    }

    public String getUserEmail() {
        return userEmail;
    }

    public void setUserEmail(String userEmail) {
        this.userEmail = userEmail;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }
}