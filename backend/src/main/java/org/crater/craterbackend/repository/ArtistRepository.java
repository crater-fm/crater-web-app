package org.crater.craterbackend.repository;

import org.crater.craterbackend.model.Artist;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ArtistRepository extends JpaRepository<Artist, Integer> {

}