import React from 'react';

import '../styles/game.css'

const game = () => {
    return(
        <div className="game">
            <div className="header">
                <button className="menu">
                    <p>Menu</p>
                </button>

                <div className="timer">
                    <p>Timer</p>
                </div>

                <div className="lives">
                    <p>❤</p>
                    <p>❤</p>
                    <p>❤</p>
                </div>
            </div>
        </div>
    )
}

export default game;