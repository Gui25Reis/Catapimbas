import React, { useState, useEffect }from 'react';

import '../styles/game.css'

import Card from '../components/card';
import Player from '../components/player';

const Game = () => {
    const Timer = () => {
        const initialSeconds = 60;
        const [seconds, setSeconds] = useState(initialSeconds);
        useEffect(()=>{
        let myInterval = setInterval(() => {
                if (seconds > 0) {
                    setSeconds(seconds - 1);
                }
                if (seconds === 0) {
                    setSeconds(60);
                } 
            }, 1000)
            return ()=> {
                clearInterval(myInterval);
              };
        }, [seconds]);
    
        return (
            <div className="timer">               
                <p>{seconds}</p> 
            </div>
        )
    }

    const listItems = (life) => {
        let numbers = new Array(life).fill("❤️");
        if(numbers.length === 0)
            return (
                <div>
                    <p>{"❌"}</p>
                </div>
            )         
        return (
            <div className="lives" id="life">
                {numbers.map((life, index) => <p key={index}> {life} </p>)} 
            </div>
        );  
    }

    function CreateMessage(e) {
        e.preventDefault();
        let chat = document.getElementById("key")
        var newMessage = document.createElement("p");
        let messages = document.getElementById("chatText")
        let shouldScroll;
        
        newMessage.innerHTML =  "Você: " + chat.value;
        document.getElementById("chatText").appendChild(newMessage);
        chat.value = '';

        shouldScroll = messages.scrollTop + messages.clientHeight === messages.scrollHeight;
        if (!shouldScroll) {
            messages.scrollTop = messages.scrollHeight;
        }
    }

    function changeChat(e){
        let chat = document.getElementById("chat");
        let messages = document.getElementById("chatText")
        
        if(e === true){
            chat.style.backgroundColor = "wheat"
            messages.style.overflowY = "scroll";
            for (let i = 0; i < messages.children.length; i++) 
                messages.children[i].style.color = "black"
        }
        else if(e === false) {
            chat.style.backgroundColor = "#00000000";
            messages.style.overflowY = "hidden";
            for (let i = 0; i < messages.children.length; i++) 
                messages.children[i].style.color = "#00000000"
        }
    }

    document.addEventListener('keydown', (e) => {
        if(e.key === "Enter"){
            changeChat(true)
        }
    })

    document.addEventListener('click', (e) => {
        
        if(e.target.tagName === "INPUT"){
            changeChat(true)
        }
        else
            changeChat(false)
    })

    return(
        <div className="game">
            <div className="header">
                <button className="menu">
                    <p>Menu</p>
                </button>

                <div>
                    {Timer()}
                </div>

                <div className="lives" id="playerLives">
                    {listItems(3)}
                </div>
            </div>

            <div id="main">
                <div id="table">

                </div>          

                <div id="mainPlayer">
                    <Player name="NomeDoJogador2" life={3}  />
                </div>

                <div id="player0">
                   <Player name="NomeDoJogador" life={3} />
                </div>
                <div id="player1">
                    <Player name="NomeDoJogador" life={3} />
                </div>
                <div id="player2">
                    <Player name="NomeDoJogador" life={3} />
                </div>
                <div id="player3">
                    <Player name="NomeDoJogador" life={3} />
                </div>
                <div id="player4">
                    <Player name="NomeDoJogador" life={3} />
                </div>
                <div id="player5">
                    <Player name="NomeDoJogador" life={3} />
                </div>
                <div id="player6">
                    <Player name="NomeDoJogador" life={3} />
                </div>        
                <div id="player7">
                    <Player name="NomeDoJogador" life={3} />
                </div>
                <div id="player8">
                    <Player name="NomeDoJogador" life={3} />
                </div>

            </div>

            <div className="footer">
                <div id="chat">
                    <div id="chatText">
                        
                    </div>

                    <div className="chatFooter">
                            <form onSubmit={CreateMessage}> 
                                <input 
                                    className="chatInput" 
                                    type="text"
                                    id="key"
                                    autoComplete="off"
                                    placeholder="Digite uma mensagem">                            
                                </input>
                                <input
                                    className="buttonInput" 
                                    type="submit"
                                    value="➤"
                                ></input>
                            </form>
                    </div>
                </div>
                
                <div className="cards">
                    <Card type="E10" />
                    <Card type="C10" />
                    <Card type="P10" />
                    <Card type="O10" />
                </div>
            </div>
        </div>
    )
}

export default Game;