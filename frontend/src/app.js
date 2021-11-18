import React from 'react';
import './index.css';
import Searchbar from './Searchbar'
import ResultsList from './ResultsList'
import Filter from './Filter'
import LoginControl from './LoginControl.js'
import axios from "axios";

// TODO: figure out how to use React Native Safe Area Context

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            searchValue: '',
            searchResults: [],
            loading: true
        };
        this.handleSearchValueChange = this.handleSearchValueChange.bind(this);
        this.handleSearchValueSubmit = this.handleSearchValueSubmit.bind(this);
    }

    handleSearchValueChange(value) {
        this.setState({ searchValue: value })
    }

    handleSearchValueSubmit(event) {
        const searchValue = this.state.searchValue;

        event.preventDefault();
        axios.get(`http://127.0.0.1:8000/api/search/${searchValue}`)
            .then((res) => {
                this.setState({searchResults: res.data});
            })
            .catch(function (error) {
                // handle error
                console.log(error);
            })
    }



    render() {




        /* TEST DATA - USE TO DESIGN API
        const searchResults = [
            {
                type: 'Artist',
                id: 3044,
                name: 'Four Tet',
                date: null,
                platform: null,
                ntsLink: 'https://www.nts.live/artists/408-four-tet',
                spotifyLink: 'spotify:artist:7Eu1txygG6nJttLHbZdQOh',
                spotifyWebLink: 'https://open.spotify.com/artist/7Eu1txygG6nJttLHbZdQOh',
                youtubeLink: 'https://www.youtube.com/results?search_query=four+tet'
            },
            {
                type: 'DJ',
                id: 4720,
                name: 'Four Tet',
                date: null,
                platform: null,
                ntsLink: 'https://www.nts.live/shows/four-tet',
                spotifyLink: 'spotify:artist:7Eu1txygG6nJttLHbZdQOh',
                spotifyWebLink: 'https://open.spotify.com/artist/7Eu1txygG6nJttLHbZdQOh',
                youtubeLink: 'https://www.youtube.com/results?search_query=four+tet'
            },
            {
                type: 'Episode',
                id: 4323,
                name: 'Four Tet and Floating Points',
                date: '16/03/17',
                platform: 'NTS Radio',
                ntsLink: 'https://www.nts.live/shows/four-tet/episodes/four-tet-and-floating-points-16th-march-2017',
                spotifyLink: null,
                spotifyWebLink: null,
                youtubeLink: null
            },
            {
                type: 'Episode',
                id: 246,
                name: 'Four Tet and Floating Points (Live at Brilliant Corners)',
                date: '10/07/17',
                platform: 'NTS Radio',
                ntsLink: 'https://www.nts.live/shows/four-tet/episodes/four-tet-and-floating-points-live-from-brilliant-corners-10th-july-2017',
                spotifyLink: null,
                spotifyWebLink: null,
                youtubeLink: null
            },
        ]
        */


        const searchValue = this.state.searchValue;
        const searchResults = this.state.searchResults;

        return (
            <div className="container">
                <div className="page-header">
                    <h1>Crater</h1>
                    <LoginControl />
                    <p>Your portal to music discovery.</p>
                    <Searchbar searchValue={searchValue} onSearchValueChange={this.handleSearchValueChange} onSearchValueSubmit={this.handleSearchValueSubmit} />
                </div>
                <div>
                    <Filter />
                    <ResultsList searchResults={searchResults} searchValue={searchValue} />
                </div>
            </div>
        )
    }
}
export default App