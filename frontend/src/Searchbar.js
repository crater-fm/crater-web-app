import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

const Searchbar = ({ keyword }) => {
    return (
        <input
            className="searchbar"
            type="search"
            key="random1"
            value={keyword}
            placeholder={"Search for an Artist, DJ, Episode, Genre or Song"}
        />
    );
}

export default Searchbar