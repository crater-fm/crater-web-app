import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

function LoginButton(props) {
    return (
        <button onClick={props.onClick}>
            Login
        </button>
    );
}

export default LoginButton