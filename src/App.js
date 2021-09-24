import './App.css';
import './styles/fonts.css'

function App() {
  
  return (
    <div className="App">
        <h1>Catapimbas</h1>
      <div className="buttons">
        <button className="createRoom">Criar Sala</button>
        <div className="enterRoom">
          <form>
            <input type="text" id="key" name="key" placeholder="Coloque o código" />
          </form>
          <button>(☞ﾟヮﾟ)☞</button>
        </div>
      </div>
    </div>
  );
}

export default App;
