import React, { Component } from 'react'
import { NavLink } from 'react-router-dom'

import _style from './_header.scss'
import HeaderImage from '../static/images/header.png'

class Header extends Component {
    render() {
        return (
            <div className='header'>
                <span className={'header-image'}>
                    <img alt='The Student Dealer' src={HeaderImage} />
                </span>

                <span className={'navbar'}>
                    <NavLink
                            exact
                            to='/'
                            className={'nav-link'}
                            activeClassName={'nav-link-active'}>
                        Home
                    </NavLink>

                    <NavLink
                            to='/deals'
                            className={'nav-link'}
                            activeClassName={'nav-link-active'}>
                        Deals
                    </NavLink>

                    <NavLink
                            to='/businesses'
                            className={'nav-link'}
                            activeClassName={'nav-link-active'}>
                        Businesses
                    </NavLink>

                    <NavLink
                            to='/mission'
                            className={'nav-link'}
                            activeClassName={'nav-link-active'}>
                        Our mission
                    </NavLink>
                </span>
            </div>
        )
    }
}

export default Header
