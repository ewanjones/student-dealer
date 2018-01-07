import React, { Component } from 'react';
import { Switch, Route } from 'react-router-dom'

import Main from './Main.jsx'
import Header from './Header.jsx'
import Signup from '../routes/Signup/Signup.jsx'

import '../styles/base.scss'


class App extends Component {
    render() {

        const mainApp = (
            <div>
                <Header />
                <Main />
            </div>
        )

        return (
            <Switch>
                <Route path="/signup" component={Signup}></Route>
                <Route path="/" render={() => mainApp}></Route>
            </Switch>
        );
    }
}

export default App;
