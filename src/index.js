import React from 'react';
import ReactDOM from 'react-dom';
import './styles/index.css';

import App from './game/App.js';
import Create from './game/Create.js'
import Game from  './game/game.js'


ReactDOM.render(
  <React.StrictMode>
    <Game/>
  </React.StrictMode>,
  document.getElementById('root')
);

