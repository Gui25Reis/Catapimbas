import React, { useState } from "react";

import {
  Link,
  withRouter
} from 'react-router-dom';

import '../sass/app.css'
import "../styles/fonts.css";

const Menu = () => {
  const [isNameFocused, setIsNameFocused] = useState(false);
  const [name, setName] = useState(0);

  const [isCodeFocused, setIsCodeFocused] = useState(false);
  const [code, setCode] = useState(0);

  function handleInputFocus(e) {
    if(e.target.id === 'playerName')
      setIsNameFocused(true);
    else
      setIsCodeFocused(true);
  }
  
  function handleInputBlur(e) {
    if(e.target.id === 'playerName')
      setIsNameFocused(false);
    else
      setIsCodeFocused(false);
  }

  function handleInputChange(e) {
    var input = document.getElementById(e.target.id).value.length;
    if(e.target.id === "key")
      setCode(input);
    else
      setName(input)
  }

  function handleKeyDown(event) {
    const badCharacter = ' ';
    if(event.nativeEvent.key === badCharacter){
      event.preventDefault();
    }
  }

  return (
  <div className="Menu">
    <h1>Catapimbas</h1>
    <form id="informations">
      <input
        required
        type="text"
        id="playerName"
        name="key"
        maxLength="15"
        autoComplete="off"
        pattern="[a-zA-Z0-9]+"
        placeholder="Coloque o nome"
        onFocus={handleInputFocus}
        onBlur={handleInputBlur}
        onInput={handleInputChange}
        onKeyDownCapture={handleKeyDown}
        style = {isNameFocused ? {backgroundColor: "#83bfe2"} : {}}
      />
      <div id="rooms"> 
        <Link to="/create">
          <input 
            type="button"
            id="createRoom"
            value="Criar Sala"
          />
        </Link>
        <div id="codeInput"> 
          <input
            required
            type="text"
            id="key"
            name="key"
            autoComplete="off"
            maxLength="5"
            pattern="[a-zA-Z0-9]+"
            placeholder="Coloque o código"
            onFocus={handleInputFocus}
            onBlur={handleInputBlur}
            onInput={handleInputChange}
            onKeyDownCapture={handleKeyDown}
            style = {isCodeFocused ? {backgroundColor: "#83bfe2"} : {}}
          />
          <Link to={code === 5 && name > 0 ? "/game" : '#'}> 
            <input 
              type="submit"
              id = "pointerButton"
              value = "➜"
              style = {code === 5 ? {cursor: 'pointer', color: "#000", fontWeight: "bold"} : {color: "#757575"}} 
            > 
            </input>
          </Link>
        </div>
      </div>
    </form>
  </div>
  );
}

export default withRouter(Menu);

