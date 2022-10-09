import { GameCard } from "./GameCard";

import { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [games, setGames] = useState([]);

  useEffect(() => {
    fetch("/games").then((res) =>
      res.json().then((data) => {
        setGames(data);
      })
    );
  }, []);

  return (
    <div className="App">
      <div className="titleContainer">Error 404 AppName not found</div>
      <div className="backContainer">
        <div className="container">
          {games.map((game) => {
            return <GameCard game={game} />;
          })}
        </div>
      </div>
    </div>
  );
}

export default App;
