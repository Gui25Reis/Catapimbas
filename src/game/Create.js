import React from "react";

import "../styles/Create.css"
import "../styles/fonts.css";

function Create() {
    return(
        <div className="createRoom">
            <div className="fundoMenu">
                <h1 className="titulo">Catapimbas</h1>
                <div className="menu"> 
                    <div className="senha">
                        <p>Criar Senha:</p>
                        <input id="senha" placeholder="Coloque a Senha"></input>
                    </div>
                    <div className="qtd">
                        <p>N.º de Jogadores:</p>
                        <select id="qtdJogadores">
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
                </div>
            </div>
        </div>
    )
}

export default Create;