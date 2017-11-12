import React, { Component } from 'react'
import TamperImg from '../../static/images/tamper.jpg'

import _style from './_card.scss'

class Card extends Component {
    render() {
        return (
            <div className={'col-sm-6-offset-1 card'}>
                <div className={'row'}>
                    <div className={'col-sm'}>
                        <img
                            alt={'Tamper'}
                            src={TamperImg}
                        />
                    </div>

                    <div className={'col-sm'}>
                        <div className={'title'}>
                            {this.props.name}
                        </div>
                        <div className={'address'}>
                            {this.props.address}
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}

export default Card
