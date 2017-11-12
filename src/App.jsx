import React, { Component } from 'react';

import Main from './Main.jsx'
import Header from './Header.jsx'

import './styles/base.scss'


class App extends Component {
    render() {
        return (
            <div>
                <Header />
                <Main />
            </div>
        );
    }
}

export default App;
