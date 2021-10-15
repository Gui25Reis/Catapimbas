import React from 'react';

import '../styles/card.css';

const Card = (props) => {
    return(
        <div className="carta" id={props.type}>
            <img 
                src={require(`../assets/Cartas/${props.type}.svg`).default} 
                alt="Carta"
                id = "teste"
                draggable="false" 
                onClick={() => {
                    var el = document.getElementById(props.type)
                    // createcard(props.type)
                    el.remove();
                }}
            />
        </div>
    )
}

export default Card;