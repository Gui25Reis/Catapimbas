import React, { useState } from "react";

import "./styles/Menu.css";
import "./styles/fonts.css";

function Menu() {
  const [isNameFocused, setIsNameFocused] = useState(false);
  const [isCodeFocused, setIsCodeFocused] = useState(false);
  const [count, setCount] = useState(0);

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

  function handleInputChange() {
    var input = document.getElementById('key').value.length;
    setCount(input);
  }

  function handleKeyDown (event) {
    const badCharacter = ' ';
    if(event.nativeEvent.key === badCharacter){
      event.preventDefault();
    }
  }

  return (
  <div className="Menu">
    <h1>Catapimbas</h1>
    <form id="informations">
      {/* <label for="name">Coloque o nome:</label> */}
      <input
        type="text"
        id="playerName"
        name="key"
        autoComplete="off"
        pattern="[a-zA-Z0-9]+"
        placeholder="Coloque o nome"
        onFocus={handleInputFocus}
        onBlur={handleInputBlur}
        onInputCapture={handleInputChange}
        onKeyDownCapture={handleKeyDown}
        style = {isNameFocused ? {backgroundColor: "#83bfe2"} : {}}
      />
      <div id="rooms"> 
        <input 
          type="button"
          id="createRoom"
          value="Criar Sala"
        />
        <div id="codeInput"> 
          <input
            type="text"
            id="key"
            name="key"
            autoComplete="off"
            maxLength="5"
            pattern="[a-zA-Z0-9]+"
            placeholder="Coloque o código"
            onFocus={handleInputFocus}
            onBlur={handleInputBlur}
            onInputCapture={handleInputChange}
            onKeyDownCapture={handleKeyDown}
            style = {isCodeFocused ? {backgroundColor: "#83bfe2"} : {}}
          />

          <input 
            type="button"
            id = "pointerButton"
            value = "➜"
            style = {count === 5 ? {cursor: 'pointer', color: "#000", fontWeight: "bold"} : {color: "#757575"}} 
          />
        </div>
      </div>
    </form>
  </div>
  );
}

export default Menu;

