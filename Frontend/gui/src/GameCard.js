import "./GameCard.css";

export function GameCard({ game }) {
  console.log(game);
  return (
    <div className="cardContainer" style={{ background: "#aeb0b0" }}>
      <div className="imageContainer">
        <img src={game.Image} alt="" />
      </div>
      <div className="cardContent">
        <div>
          <h3>{game.Name}</h3>
        </div>
        <div>
          <p>Precio Amazon: ${game.AmazonPrice}</p>
          <p>Precio PS Store: ${game.PlayStationPrice}</p>
          <p>Puntuacion Metacritic: {game.MetaScore}</p>
          <p>How Long to beat {game.HowLongtoBeat}</p>
        </div>
      </div>
    </div>
  );
}
