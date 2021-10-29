import React from 'react';

import '../styles/minicard.css';

const MiniCard = (props) => {
    return(
        <div className="miniCarta" id={`${props.type}Mini`}>
            <img 
                src={require(`../assets/MiniCartas/${props.type}.svg`).default} 
                alt="MiniCarta"
                draggable="false" 
                style={props.honeydew === true ? {opacity: "0.5"} : {opacity: "1"}}
            />
        </div>
    )
}

export default MiniCard;