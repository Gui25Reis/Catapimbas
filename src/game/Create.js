import React from "react";

import "../styles/Create.css"
import "../styles/fonts.css";

function Create() {
    return(
        <div className="createRoom">
            <h1>Catapimbas</h1>
            <div className="menu">
                <div className="menuOptions">
                    <div className="qtPlayers">
                        <p>N.º de Jogadores:</p>
                        <select id="players">
                            <option>2</option>
                            <option>3</option>
                            <option>4</option>
                            <option>5</option>
                            <option>6</option>
                            <option>7</option>
                            <option>8</option>
                            <option>9</option>
                            <option>10</option>
                        </select>
                    </div>
                    <div className="qtLives">
                    <p>N.º de Vidas:</p>
                    <select id="lives">
                            <option>1</option>
                            <option>2</option>
                            <option>3</option>
                            <option>4</option>
                            <option>5</option>
                        </select>
                    </div>
                </div>
                <div className="menuButtons">
                    <button className="back">Voltar</button>
                    <button className="buttonCreate">Criar Sala</button>
                </div>
            </div>
        </div>
    )
}

export default Create;