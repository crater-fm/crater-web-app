import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './index.scss';
import ArtistResult from './ArtistResult.js'
import DjResult from './DjResult.js'
import EpisodeResult from './EpisodeResult.js'
import SongResult from './SongResult.js'


const ListHeader = (props) => {
        const searchResults = props.searchResults;
        const searchString = props.searchString;
        return (
            <h3>{searchResults.length} search results for {searchString}</h3>
        )
}

    const ListBody = (props) => {

        const rows = props.searchResults.map((row, index) => {
            switch (row.type) {
                case 'Artist':
                    return (<ArtistResult key={index} value={row} />);
                case 'DJ':
                    return (<DjResult key={index} value={row} />);
                case 'Episode':
                    return (<EpisodeResult key={index} value={row} />);
                case 'Song':
                    return (<SongResult key={index} value={row} />);
                default:
                    return (<p>Entry does not have a valid search result type</p>)
            }
        })
        return <ul>{rows}</ul>
    }

    class ResultsList extends Component {
        render() {
            const { searchResults } = this.props
            const { searchString } = this.props

            return (
                <div className="results">
                    <ListHeader searchResults={searchResults} searchString={searchString} />
                    <br></br>
                    <ListBody searchResults={searchResults} searchString={searchString} />
                </div>
            )
        }
    }

    export default ResultsList