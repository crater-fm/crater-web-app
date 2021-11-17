import React, { Component } from 'react';
import './index.css';
import Icons from './Icons.js'

class ArtistResult extends Component {
    render () {
        const value = this.props.value;
        return (
            <li className='artist'>
                <div className='info'>
                    <h6>Artist</h6>
                    <p>{value.artist_name}</p>
                </div>
                <div className='links'>
                    {/* TODO: add Icon function once links are added to database & API
                     <Icons value={value} /> */}
                </div>
            </li>
        )
    }
}


export default ArtistResult