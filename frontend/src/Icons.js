import React, { Component } from 'react';
import './index.css';
import ntsIcon from './img/nts_icon.png'
import spotifyIcon from './img/Spotify_Icon_RGB_Black.png'
import youtubeIcon from './img/yt_icon_mono_light.png'

const SpotifyIcon = (props) => {
    const value = props.value;
    if (value.spotifyWebLink) {
        return (
            <a href={value.spotifyWebLink}><img src={spotifyIcon} alt='Open in Spotify' className='icon'></img></a>
        )
    } else {
        return null
    }
}

const NtsIcon = (props) => {
    const value = props.value;
    if (value.episode_url && value.episode_url.includes('nts.live')) {
        return (
            <a href={value.episode_url}><img src={ntsIcon} alt='Open in NTS Radio' className='icon'></img></a>
        )
    } else {
        return null
    }
}

const YoutubeIcon = (props) => {
    const value = props.value;
    if (value.youtubeLink) {
        return (
            <a href={value.youtubeLink}><img src={youtubeIcon} alt='Search on Youtube' className='icon'></img></a>
        )
    } else {
        return null
    }
}


class Icons extends Component {
    render() {
        const value = this.props.value;
        return (
            <div className="icons">
                <SpotifyIcon value={value} />
                <NtsIcon value={value} />
                <YoutubeIcon value={value} />
            </div>
        )
    }
}


export default Icons