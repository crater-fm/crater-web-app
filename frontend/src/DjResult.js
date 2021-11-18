import React, { Component } from 'react';
import './index.css';
import Icons from './Icons.js'

class DjResult extends Component {
    render() {
        const value = this.props.value;
        return (
            <li className='dj'>
                <div className='info'>
                    <h6>DJ</h6>
                    <p>{value.dj_name}</p>
                </div>
                <div className='links'>
                     <Icons value={value} />
                </div>
            </li>
        )
    }
}

export default DjResult