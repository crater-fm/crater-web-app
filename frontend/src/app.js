import React from 'react';
import ReactDOM from 'react-dom';
import './index.scss';
import Searchbar from './Searchbar'
import ResultsTable from './ResultsTable'
import ResultsList from './ResultsList'
import Filter from './Filter'

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
        
        
        
        return (
            <div className="container">
                <h1>Welcome to Crater!</h1>
                <p>Your portal to music discovery.</p>
                <br></br>
                <br></br>
                <Filter />
                <Searchbar />
                <br></br>
                <br></br>
                <ResultsList searchResults={searchResults} searchString={searchString}/>
            </div>
        )
    }
}
export default App