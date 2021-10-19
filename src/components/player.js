import React, { useState } from 'react';

import '../styles/player.css';
import playerCard from '../assets/Usuario/Usuario.png';

const Player = (props) => {
    const [numbers] = useState(Array(props.life).fill("❤️")) 

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
    return (
        <div className="player" >
            <p>{props.name}</p>
            <img src={playerCard} alt="imagem dos jogadores" draggable="false"></img>
            {listItems()}
            
        </div>
      
    );
}

export default Player;