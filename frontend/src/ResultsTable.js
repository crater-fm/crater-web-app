import React from 'react';
import ReactDOM from 'react-dom';
import './index.scss';
import {
    StructuredListWrapper,
    StructuredListHead,
    StructuredListBody,
    StructuredListRow,
    StructuredListInput,
    StructuredListCell,
} from 'carbon-components-react';
import ntsIcon from './img/nts_icon.png'
import spotifyIcon from './img/Spotify_Icon_RGB_Black.png'
import youtubeIcon from './img/yt_icon_mono_light.png'

const TableHeader = () => {
    return (
        <StructuredListHead>
            <StructuredListRow head>
                <StructuredListCell head>Type</StructuredListCell>
                <StructuredListCell head>Result</StructuredListCell>
            </StructuredListRow>
        </StructuredListHead>
    )
}

const TableBody = (props) => {

    const rows = props.searchResults.map((row, index) => {
        return (
            <StructuredListRow key={index}>
                <StructuredListCell noWrap>{row.type}</StructuredListCell>
                <StructuredListCell noWrap>{row.name}</StructuredListCell>
                <StructuredListCell noWrap>
                    <a href={row.ntsLink} target="_blank">
                        <img src={ntsIcon} alt="NTS Radio" className="icon">
                        </img>
                    </a>
                    <a href={row.spotifyWebLink} target="_blank">
                        <img src={spotifyIcon} alt="Open in Spotify" className="icon">
                        </img>
                    </a>
                    <a href={row.youtubeLink} target="_blank">
                        <img src={youtubeIcon} alt="Open in Youtube" className="icon">
                        </img>
                    </a>
                </StructuredListCell>
            </StructuredListRow>
        )
    })

    return <StructuredListBody>{rows}</StructuredListBody>
}

class ResultsTable extends React.Component {
    render() {
        const { searchResults } = this.props

        return (
            <div className="ResultsTable">
                <StructuredListWrapper ariaLabel="Search results">
                    <TableHeader />
                    <TableBody searchResults={searchResults} />
                </StructuredListWrapper>
            </div>

        )
    }
}

export default ResultsTable