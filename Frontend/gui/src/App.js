import { GameCard } from "./GameCard";
import { games as data } from "./games";
import { useState, useEffect } from "react";
import './App.css';

function App() {
  console.log(data);
  const [games, setGames] = useState([]);

  useEffect(() => {
    setGames(data);
  }, []);

  if (games.length === 0) {
    return <h1>No hay juegos</h1>;
  }

  return (
    <div className="App">
      <div className="container">
        {games.map((game) => {
          return (
            <GameCard game = {game}/>
          );
        })}
      </div>
    </div>
  );
}

export default App;
