import React, { Component } from 'react'
import { Switch, Route } from 'react-router-dom'

import _style from './_main.scss'

import Home from '../routes/Home/Home.jsx'
import Businesses from '../routes/Businesses/Businesses.jsx'

class Main extends Component {
    render() {
        return (
            <div className={'main-window'}>
                <Switch>
                    <Route exact path="/" component={Home}></Route>
                    <Route path="/businesses" component={Businesses}></Route>
                </Switch>
            </div>
        )
    }
}

export default Main
