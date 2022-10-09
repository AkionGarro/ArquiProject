import "./GameCard.css";

export function GameCard({ game }) {
  console.log(game);
  return (
    <div className="cardContainer" style={{ background: "#366666" }}>
      <div className="imageContainer">
        <img src={game.Image} alt="" />
      </div>
      <div className="cardContent">
        <div className="gameName">
          <h3>{game.Name}</h3>
        </div>
        <div className="gameInfo">
          <p>Precio Amazon: ${game.AmazonPrice}</p>
          <p>Precio PS Store: ${game.PlayStationPrice}</p>
          <p>Puntuacion Metacritic: {game.MetaScore}</p>
          <p>Duracion aprox: {game.HowLongtoBeat}</p>
        </div>
      </div>
    </div>
  );
}
