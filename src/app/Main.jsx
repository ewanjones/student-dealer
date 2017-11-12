import React, { Component } from 'react'
import { Switch, Route } from 'react-router-dom'

import Home from '../routes/Home/Home.jsx'
import Businesses from '../routes/Businesses/Businesses.jsx'

class Main extends Component {
    render() {
        return (
            <Switch>
                <Route exact path="/" component={Home}></Route>
                <Route path="/businesses" component={Businesses}></Route>
            </Switch>
        )
    }
}

export default Main
