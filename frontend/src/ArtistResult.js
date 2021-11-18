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
                    <a href='http://www.drewnollsch.com'>{value.artist_name}</a>
                </div>
                <div className='links'>
                     <Icons value={value} />
                </div>
            </li>
        )
    }
}


export default ArtistResult