import React from 'react';
import ReactDOM from 'react-dom';

import {
  BrowserRouter as Router,
  Route,
} from 'react-router-dom';

// import './styles/index.css';

import Create from './game/Create.js'
import Menu from './game/Menu.js';
import Game from  './game/Game.js'

ReactDOM.render(
  <React.StrictMode>
    <Router>
      <div>
        <Route exact path="/">
          <Menu />
        </Route>
        <Route path="/game">
          <Game />
        </Route>
        <Route path="/create">
          <Create />
        </Route>
      </div>
    </Router>
  </React.StrictMode>,
  document.getElementById('root')
);

