import { GameCard } from "./GameCard";

import { useState, useEffect } from "react";
import './App.css';

function App() {
  const [games, setGames] = useState([]);

  useEffect(() => {
        fetch("/games").then((res) =>
            res.json().then((data) => {
              setGames(data)
            })
        );
    }, []);

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
