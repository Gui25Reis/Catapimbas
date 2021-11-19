import React, { useState } from 'react';

import '../sass/app.css'
import playerCard from '../assets/Usuario/Usuario.png';
import cardBack from '../assets/cardBack.png';

const Player = (props) => {
    const [numbers] = useState(Array(props.life).fill("❤️")) 
    const [usePlayer] = useState(props.player)

    const listItems = () => {
        if(numbers.length === 0){
            return (
                <div className="playerslives" id="life">
                    <p>{"❌"}</p>
                </div>
            )
        }
        return (
            <div className="playerslives" id="life">
                {numbers.map((life, index) => <p key={index}> {life} </p>)} 
            </div>
        );
    }

    const playerOff = (param) => {
        return(
            <div className="playerOffline" >
                {/* <p className="playerNameOff">{param.name}</p> */}
                <div className="playerProfileOff" >
                    <img 
                        className="playerImageOff" 
                        src={playerCard} 
                        alt="imagem dos jogadores" 
                        draggable="false"
                    >
                    </img>
                </div>
                {/* {listItems()} */}
            </div>
        )
    }


    const playerOn = (param) => {
        return(
            <div className="player" >
                <p className="playerName">{param.name}</p>
                <div className="playerProfile" >
                    <img 
                        className="playerImage" 
                        src={playerCard} 
                        alt="imagem dos jogadores" 
                        draggable="false"
                        style={param.host === true ? {borderColor: "#41d4b0"} : {borderColor: "#1c0c16"}}>
                    </img>
                    <div className="cardsNumbers">
                        <img className="cardsBack" src={cardBack} alt="costas da carta" draggable="false"></img>
                        <p>{param.cards === undefined ? "0" : param.cards}</p>
                    </div>
                </div>
                {listItems()}
            </div>
        )
    }
    return (
        usePlayer ? playerOn(props) : playerOff(props)
    );
}

export default Player;