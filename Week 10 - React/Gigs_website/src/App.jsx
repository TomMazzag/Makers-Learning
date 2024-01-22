import Hello from "./components/Hello";
import makersLogo from "./assets/Makers-Logo.png";
import "./App.css";
import Gig from "./components/Gig";
import gigsList from "./gigsList.js";

function App() {
  return (
    <>
      <img className="logo" src={makersLogo}></img>
      <Hello title="Available Concerts" />
      {gigsList.map((gig) => (
        <Gig 
        band = {gig.band}
        imageURL = {gig.imageURL}
        description = {gig.description}
        dateTime = {gig.dateTime}
        venue = {gig.venue}/>
      ))}
    </>
  );
}

export default App;
