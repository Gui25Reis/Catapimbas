import React, { useState, useEffect } from 'react';

import '../sass/app.css'

import Card from '../components/Card';
import MiniCard from '../components/MiniCard';
import Player from '../components/Player';

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
        let chat = document.getElementById("message")
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

        console.log(chat)
        
        if(e === true){
            chat.style.backgroundColor = "wheat"
            messages.style.overflowY = "scroll";
            for (let i = 0; i < messages.children.length; i++) 
                messages.children[i].style.color = "black"
        }
        else if(e === false && chat !== null) {
            chat.style.backgroundColor = "#00000000";
            messages.style.overflowY = "hidden";
            for (let i = 0; i < messages.children.length; i++) 
                messages.children[i].style.color = "#00000000"
        }
    }

    // const createMiniCard = (card) => {        
    //     return(
    //         <MiniCard type= {`${card}Mini`} honeydew={false} />
    //     )
    // }

    // function teste(e){
    //     if(e.target.className === "imgCard"){
    //         createMiniCard(e.target.id)
    //     }
    // }

    const [card, setCard] = useState(false);

    document.addEventListener('keydown', (e) => {
        if(e.key === "Enter"){
            changeChat(true)
        }
    })

    document.addEventListener('click', (e) => {
        console.log(e);
        if(e.target.className === "chatInput" || e.target.className === "buttonInput"){
            changeChat(true)
        }
        else
            changeChat(false)
    })

    return(
        <div className="game">
            <div className="header">
                <div className="headerMenu">
                    <button className="buttonMenu">
                        <p>Menu</p>
                    </button>
                </div>

                <div>
                    {Timer()}
                </div>

                <div className="lives" id="playerLives">
                    {listItems(3)}
                </div>
            </div>

            <div id="main">
                <div id="table">
                    <div id="turned">
                        <MiniCard type="C01Mini" honeydew={false} />
                    </div>
                    <div id="mainCard">
                        {/* {createMiniCard} */}
                        {/* <MiniCard type="P02Mini" honeydew={true} /> */}
                    </div>
                    <div id="card0">
                        <MiniCard type="P02Mini" honeydew={true} />
                    </div>
                    <div id="card1">
                        <MiniCard type="E03Mini" honeydew={true} />
                    </div>
                    <div id="card2">
                        <MiniCard type="C04Mini" honeydew={false} />
                    </div>
                    <div id="card3">
                        <MiniCard type="E05Mini" honeydew={false} />
                    </div>
                    <div id="card4">
                        <MiniCard type="E06Mini" honeydew={false} />
                    </div>
                    <div id="card5">
                        <MiniCard type="O07Mini" honeydew={false} />
                    </div>
                    <div id="card6">
                        <MiniCard type="P03Mini" honeydew={true} />
                    </div>
                    <div id="card7">
                        <MiniCard type="C02Mini" honeydew={true} />
                    </div>
                    <div id="card8">
                        <MiniCard type="O04Mini" honeydew={true} />
                    </div>
                </div>          

                <div id="player0">
                   <Player player={true} host={true} name="NomeDoJogador" life={3} cards="4" />
                </div>
                <div id="player1">
                    <Player player={true} name="NomeDoJogador" life={3} cards="5" />
                </div>
                <div id="player2">
                    <Player player={true} name="NomeDoJogador" life={3} cards="4" />
                </div>
                <div id="player3">
                    <Player player={true} name="NomeDoJogador" life={3} cards="4" />
                </div>
                <div id="player4">
                    <Player player={true} name="NomeDoJogador" life={3} cards="4" />
                </div>
                <div id="player5">
                    <Player player={true} name="NomeDoJogador" life={3} cards="4" />
                </div>
                <div id="player6">
                    <Player player={true} name="NomeDoJogador" life={3} cards="3" />
                </div>        
                <div id="player7">
                    <Player player={false} name="NomeDoJogador" life={3} cards="3" />
                </div>
                <div id="player8">
                    <Player player={true} name="NomeDoJogador" life={3} cards="4" />
                </div>
                <div id="player9">
                   <Player player={true} name="NomeDoJogaddor" life={3} cards="4" />
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
                                    id="message"
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
                {/* onClick={teste} */}
                <div className="cards" >
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