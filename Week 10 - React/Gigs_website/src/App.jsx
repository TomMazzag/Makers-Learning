import Hello from "./components/Hello";
import makersLogo from "./assets/Makers-Logo.png";
import "./App.css";
import Gig from "./components/Gig";
//import gigsList from "./gigsList.js";
import { useState, useEffect } from 'react'
import "./assets/nbt.webp"

function App() {
  const [gigsList, setGigsList] = useState([]);

  useEffect(() => {
    const URL = "https://makers-gig-backend.onrender.com/events";
    fetch(URL)
      .then((res) => res.json())
      .then((data) => setGigsList(data));
  }, [])

  const handleFavouriteChange = (gigId, isFavourite) => {
    // Update the state of the app based on the favourite change
    const updatedGigs = gigsList.map((gig) =>
        gig.event_id === gigId ? { ...gig, favourited: isFavourite } : gig
    );
    setGigsList(updatedGigs)
  };

  const allGigs = gigsList.map((gig) => {
    return (
    <Gig 
    key = {gig.event_id}
    id = {gig.event_id}
    band = {gig.band_name}
    imageURL = "../src/assets/venue1.avif"
    description = {gig.description}
    dateTime = {gig.time}
    venue = {gig.location}
    favourited = {gig.favourited}
    onFavouriteChange={handleFavouriteChange}
    />)
    }
  )

  const favouriteGigsList = allGigs.filter(gig => gig.props.favourited);
  const nonFavouriteGigsList = allGigs.filter(gig => !gig.props.favourited);

  return (
    <>
      <img className="logo" src={makersLogo}></img>
      <Hello title="Available Concerts" />
      <div className="allGigs">
        {favouriteGigsList}
        {nonFavouriteGigsList}
      </div> 
    </>
  );
}

export default App;
