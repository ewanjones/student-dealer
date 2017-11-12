import React, { Component } from 'react'
import { NavLink } from 'react-router-dom'

import _style from './_header.scss'
import HeaderImage from '../static/images/header.png'

class Header extends Component {
    render() {
        return (
            <div className='container-fluid text-center'>
                <div className={'row header-image'}>
                    <img alt='The Student Dealer' src={HeaderImage} />
                </div>

                <div className={'container-fluid col-md-10 navbar'}>
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
                </div>
            </div>
        )
    }
}

export default Header
