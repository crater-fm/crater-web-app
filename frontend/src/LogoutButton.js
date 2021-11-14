import React from 'react';
import './index.css';

function LogoutButton(props) {
    return (
        <button onClick={props.onClick}>
        Logout
        </button>
    );
}

export default LogoutButton