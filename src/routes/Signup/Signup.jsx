import React, { Component } from 'react'

import _style from './_signup.scss'


class Signup extends Component {
    render() {
        return (
            <div className='layout'>
                <div className='signup'>
                    <div className='login'>
                        <p>Click here to log in:</p>
                        <div className='submit-btn'>
                            <button>Log in</button>
                        </div>
                    </div>

                    <p>Enter your email here to sign up!</p>

                    <input
                        className='email'
                        placeholder='Email...'
                    />

                    <div className='submit-btn'>
                        <button type='submit'>Submit</button>
                    </div>
                </div>
            </div>
        )
    }
}

export default Signup
