import React, { useState } from "react";

import "./App.css";
import "./styles/fonts.css";

function App() {
  const [isFocused, setIsFocused] = useState(false);
  const [count, setCount] = useState(0);

  function handleInputFocus() {
    setIsFocused(true);
  }
  
  function handleInputBlur() {
    setIsFocused(false);
  }

  function handleInputChange(e) {
    var input = document.getElementById('key').value.length;
    setCount(input);
  }

  function handleKeyDown (event) {
    const badCharacter = ' '
    if(event.nativeEvent.key === badCharacter){
      event.preventDefault();
    }
  }

  return (
  <div className="App">
    <h1>Catapimbas</h1>
    <div className="buttons">
      <button className="createRoom">Criar Sala</button>
      <div className="enterRoom">
        <form>
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
            style = {isFocused ? {backgroundColor: "#83bfe2"} : {}}
          />
        </form>
        <button>
          {count === 5 ? "➜" : ""}
        </button>
      </div>
    </div>
  </div>
  );
}

export default App;