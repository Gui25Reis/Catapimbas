import React from 'react';

import '../styles/card.css';

const Card = (props) => {
    return(
        <div className="card">
            <img 
                src={require(`../assets/Cartas/${props.type}.svg`).default} 
                alt="Carta"
                id={props.type}
                draggable="false" 
                className="imgCard"
                onClick={() => {
                    var el = document.getElementById(props.type)
                    el.remove();
                }}
            />
        </div>
    )
}

export default Card;