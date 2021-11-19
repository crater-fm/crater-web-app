import React, { Component } from 'react';
import './index.css';
import Icons from './Icons.js'

class DjResult extends Component {
    render() {
        const value = this.props.value;
        const djPageUrl = `http://crater.drewnollsch.com/djs/${value.dj_id}`
        return (
            <li className='dj'>
                <div className='info'>
                    <h6>DJ</h6>
                    <a href={djPageUrl}>{value.dj_name}</a>
                </div>
                <div className='links'>
                     <Icons value={value} />
                </div>
            </li>
        )
    }
}

export default DjResult