import React from 'react';
import ReactDOM from 'react-dom';
import './index.scss';
import { Checkbox } from 'carbon-components-react'

class Filter extends React.Component {
    render() {
        return (
            <div className="Filter">
                <fieldset className="bx--fieldset">
                    <legend className="bx--label">Filter by</legend>
                    <Checkbox labelText="Artist" id="checked-artist" />
                    <Checkbox labelText="DJ" id="checked-dj" />
                    <Checkbox labelText="Episode" id="checked-episode" />
                    <Checkbox labelText="Genre" id="checked-genre" />
                    <Checkbox labelText="Song" id="checked-song" />
                </fieldset>
            </div>
        )
    }
}
export default Filter