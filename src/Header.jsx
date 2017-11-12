import React, { Component } from 'react'
import { Router, Link } from 'react-router-dom'

import _style from './_header.scss'
import HeaderImage from './static/images/header.png'

class Header extends Component {
    render() {
        return (
            <div className='container-fluid text-center'>
                <div className={'row header-image'}>
                    <img alt='The Student Dealer' src={HeaderImage} />
                </div>

                <div className={'container col-sm-6'}>
                    <div className={'row'}>
                        <div className={'col-sm'}>
                            <Link
                                    to='/'
                                    activeClassName={'nav-link-active'}
                                    className={'nav-link'}>
                                Home
                            </Link>
                        </div>

                        <div className={'col-sm'}>
                            <Link
                                    to='/deals'
                                    activeClassName={'nav-link-active'}
                                    className={'nav-link'}>
                                Deals
                            </Link>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}

export default Header
