import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './index.scss';
import Icons from './Icons.js'

class GenreResult extends Component {
    render() {
        const value = this.props.value;
        return (
            <li className='genre'>
                <div className='info'>
                    <h6>{value.type}</h6>
                    <p>{value.name}</p>
                </div>
                <div className='links'>
                    <Icons value={value} />
                </div>
            </li>
        )
    }
}

export default GenreResult