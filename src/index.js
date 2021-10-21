import React from 'react';
import ReactDOM from 'react-dom';
import './styles/index.css';

// import App from './game/App.js';
// import Game from  './game/game.js'
import Create from './game/Create.js'


ReactDOM.render(
  <React.StrictMode>
    {/* <App/> */}
    <Create/>
  </React.StrictMode>,
  document.getElementById('root')
);

