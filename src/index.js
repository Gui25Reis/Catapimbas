import React from 'react';
import ReactDOM from 'react-dom';
import './styles/index.css';
// import App from './App';
import Game from  './game/game.js'


ReactDOM.render(
  <React.StrictMode>
    <Game />
  </React.StrictMode>,
  document.getElementById('root')
);

