import React, { Component } from 'react'
import TamperImg from '../../static/images/tamper.jpg'
// import _grid from '~/bootstrap/lib/grid.scss'

import _style from './_card.scss'


class Card extends Component {
    render() {
        return (
            <div className={'card'}>
                <div className={'row'}>
                    <div className={'col-sm-5'}>
                        <img
                            alt={'Tamper'}
                            src={TamperImg}
                        />
                    </div>

                    <div className={'col-sm'}>
                        <h3>
                            {this.props.name}
                        </h3>
                        <div className={'address'}>
                            {this.props.address}
                        </div>
                        <div className={'description'}>
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus in sapien tincidunt, malesuada elit vel, tincidunt massa. Interdum et malesuada fames ac ante ipsum primis in faucibus. Morbi ullamcorper neque non magna molestie lacinia. Phasellus eleifend odio felis, imperdiet lacinia sapien posuere non.
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}

export default Card
