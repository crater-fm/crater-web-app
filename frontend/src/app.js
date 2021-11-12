import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Searchbar from './Searchbar'
import ResultsList from './ResultsList'
import Filter from './Filter'
import LoginControl from './LoginControl.js'

// TODO: figure out how to use React Native Safe Area Context

class App extends React.Component {

    render() {
        const searchString = 'four tet'

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


        /* TODO: fetch data from API instead
        const performSearch = (input) => {
            fetch(`http://www.drewnollsch.com/crater/api/global/${input}`)
                .then(response => response.json())
                .then(responseData => {
                    this.setState({
                        results: responseData.results,
                        loading: false
                    });
                })
                .catch(error => {
                    console.log('Error fetching and parsing data', error);
                });
        }
        const searchResults = responseData.results;
        */

        return (
            <div className="container">
                <div className="page-header">
                    <h1>Crater</h1>
                    <LoginControl />
                    <p>Your portal to music discovery.</p>
                    <Searchbar />
                </div>
                <div>
                    <Filter />
                    <ResultsList searchResults={searchResults} searchString={searchString} />
                </div>
            </div>
        )
    }
}
export default App