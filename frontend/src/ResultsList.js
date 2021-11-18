import React, { Component } from 'react';
import './index.css';
import ArtistResult from './ArtistResult.js'
import DjResult from './DjResult.js'
import EpisodeResult from './EpisodeResult.js'


const ListHeader = (props) => {
    const searchResults = props.searchResults;
    const searchValue = props.searchValue;
    var resultsLength = 0;
    Object.entries(props.searchResults).forEach((entry) => {
        const [key, value] = entry;
        resultsLength = resultsLength + value.length
    })
    return (
        <h4 className='results-header'>{resultsLength} search results for {searchValue}</h4>
    )
}

const ListBody = (props) => {

    const resultsList = [];

    Object.entries(props.searchResults).forEach((entry) => {
        const [key, value] = entry;
        if (key === 'artists') {
            var subResults = [];
            value.forEach((element, index) => {
                subResults[index] = <ArtistResult key={index} value={element} />;
            })
        } else if (key === 'djs') {
            var subResults = [];
            value.forEach((element, index) => {
                subResults[index] = <DjResult key={index} value={element} />;
            })
        } else if (key === 'episodes') {
            var subResults = [];
            value.forEach((element, index) => {
                subResults[index] = <EpisodeResult key={index} value={element} />;
            })
        } else {
            console.log('Unrecognized data type')
        }

        if (subResults.length > 0) {
            resultsList.push(subResults);
        }
  
    })
    console.log(resultsList)




    return( <ul className='search-results'>{resultsList}</ul> )
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
 */

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