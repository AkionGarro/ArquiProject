import './GameCard.css';

export function GameCard({ game }) {
  console.log(game);
  return (
    <div className="row" key={game.Id} style={{ background: "#aeb0b0" }}>
      <h2>{game.Name}</h2>
      <div>
        <p>Precio Amazon ${game.AmazonPrice}</p>
        <p>Precio PS Store ${game.PlayStationPrice}</p>
        <p>How Long to beat {game.HowLongtoBeat}</p>
      </div>
    </div>
  );
}
