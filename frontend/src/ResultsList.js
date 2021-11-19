import React, { Component } from 'react';
import './index.css';
import ArtistResult from './ArtistResult.js'
import DjResult from './DjResult.js'
import EpisodeResult from './EpisodeResult.js'


const ListHeader = (props) => {
    const searchResults = props.searchResults;
    const searchValue = props.searchValue;
    var resultsLength = 0;
    Object.entries(searchResults).forEach((entry) => {
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

    return( <ul className='search-results'>{resultsList}</ul> )
}


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