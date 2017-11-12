import React, { Component } from 'react'
import { Switch, Router, Route, Link     } from 'react-router-dom'

import Home from './routes/Home/Home.jsx'

class Main extends Component {
    render() {
        return (
            <Switch>
                <Route exact path="/" component={Home}></Route>
                <Route path="/home" component={Home}></Route>
            </Switch>
        )
    }
}

export default Main
