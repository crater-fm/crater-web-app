import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './index.css';

class Searchbar extends Component {
    constructor(props) {
        super(props);
        this.state = {
            value: ''
        };
        // Necessary to make 'this' work in the callback
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({ value: event.target.value });
    }
    
    handleSubmit(event) {
        alert('Search database for the following: ' + this.state.value);
        event.preventDefault();
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <input
                    className="searchbar"
                    type="search"
                    value={this.state.value}
                    onChange={this.handleChange}
                    placeholder="Search for an Artist, DJ, Episode, Genre or Song"
                />
            </form>
        )
    }
}

export default Searchbar