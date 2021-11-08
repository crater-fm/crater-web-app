import React from 'react';
import ReactDOM from 'react-dom';
import './index.scss';
import { Search } from 'carbon-components-react';


class Searchbar extends React.Component {
    render() {
        return (
            <div className="Searchbar">
                <Search labelText="Crater Global Search" placeholder="Search for an artist, DJ, or song name"></Search>
            </div>
        )
    }
}

export default Searchbar