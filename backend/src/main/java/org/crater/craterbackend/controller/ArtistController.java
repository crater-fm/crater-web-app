package org.crater.craterbackend.controller;

import org.crater.craterbackend.exception.ResourceNotFoundException;
import org.crater.craterbackend.model.Artist;
import org.crater.craterbackend.repository.ArtistRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/api/v1")
public class ArtistController {
    @Autowired
    private ArtistRepository artistRepository;

    @GetMapping("/artist")
    public List<Artist> getAllArtists() {
        return artistRepository.findAll();
    }

    @GetMapping("artist/{id}")
    public ResponseEntity<Artist> getArtistById(@PathVariable(value = "id") int artistId)
        throws ResourceNotFoundException {
        Artist artist = artistRepository.findById(artistId)
                .orElseThrow(() -> new ResourceNotFoundException("Artist not found for this ID."));
        return ResponseEntity.ok().body(artist);
    }




}
