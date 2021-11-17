import React, { Component } from 'react';
import './index.css';
import ArtistResult from './ArtistResult.js'
import DjResult from './DjResult.js'
import EpisodeResult from './EpisodeResult.js'
import SongResult from './SongResult.js'
import GenreResult from './GenreResult.js'


const ListHeader = (props) => {
    const searchResults = props.searchResults;
    const searchValue = props.searchValue;
    return (
        <h4 className='results-header'>{searchResults.length} search results for {searchValue}</h4>
    )
}

const ListBody = (props) => {

    Object.entries(props.searchResults).forEach((entry) => {
        const [key, value] = entry;
        return <p>{value}</p>

        switch (key) {
            case 'artists':
                break;
            case 'djs':
                break;
            case 'episodes':
                break;
            default:
                return (<p>Entry does not have a valid search result type</p>);
        }
    }
    )
    return <ul className='search-results'>{rows}</ul>
}

/*
    const rows = props.searchResults.map((row, index) => {
        switch (row.type) {
            case 'Artist':
                // TODO: It's not recommended to use index as the key. If there is a source ID available, should use that instead
                return (<ArtistResult key={index} value={row} />);
                break;
            case 'DJ':
                return (<DjResult key={index} value={row} />);
                break;
            case 'Episode':
                return (<EpisodeResult key={index} value={row} />);
                break;
            case 'Song':
                return (<SongResult key={index} value={row} />);
                break;
            case 'Genre':
                return (<GenreResult key={index} value={row} />);
                break;
            default:
                return (<p>Entry does not have a valid search result type</p>)
        }
    })
   

    return <ul className='search-results'>{rows}</ul>
}
 * /

class ResultsList extends Component {
    render() {
        const { searchResults } = this.props
        const { searchValue } = this.props

        return (
            <div className="results">
                <ListHeader searchResults={searchResults} searchValue={searchValue} />
                <ListBody searchResults={searchResults} searchValue={searchValue} />
            </div>
        )
    }
}

export default ResultsList