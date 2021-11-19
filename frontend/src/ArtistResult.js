import React, { Component } from 'react';
import './index.css';
import Icons from './Icons.js'

class ArtistResult extends Component {
    render () {
        const value = this.props.value;
        const artistPageUrl = `http://crater.drewnollsch.com/artists/${value.artist_id}`
        return (
            <li className='artist'>
                <div className='info'>
                    <h6>Artist</h6>
                    <a href={artistPageUrl}>{value.artist_name}</a>
                </div>
                <div className='links'>
                     <Icons value={value} />
                </div>
            </li>
        )
    }
}


export default ArtistResult