import React, { Component } from 'react';
import './index.css';

class Searchbar extends Component {
    constructor(props) {
        super(props);
        // Necessary to make 'this' work in the callback
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);

    }

    
    handleChange(event) {
        this.props.onSearchValueChange(event.target.value);
    }

    handleSubmit(event) {
        this.props.onSearchValueSubmit(event);
    }



    render() {
        const searchValue = this.props.searchValue;
        return (
            <form onSubmit={this.handleSubmit}>
                <input
                    className="searchbar"
                    type="search"
                    value={searchValue}
                    onChange={this.handleChange}
                    placeholder="Search for an Artist, DJ, Episode, Genre or Song"
                />
            </form>
        )
    }
}

export default Searchbar