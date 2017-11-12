import React, { Component } from 'react'

import Card from './card.jsx'


class Businesses extends Component {
    render() {
        return (
            <div className={'container'}>
                <Card
                    name={'Cafe Red'}
                    address={'12 Crookes Road, S10 5BH'}
                />
            </div>
        )
    }
}

export default Businesses
