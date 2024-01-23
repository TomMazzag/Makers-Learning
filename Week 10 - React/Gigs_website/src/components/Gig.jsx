import './gig.css'

const Gig = (props) => {
    
    const addedToFavourite = () => {
        props.onFavouriteChange(props.id, true)
    }

    return (
        <div className="gig" key={props.id}>
           <h3 className="bandName">{props.band}</h3>
            <img src={props.imageURL} alt="" className="bandImage"/> 
            <p className="eventDescription">{props.description}</p>
            <p className="dateTime">{props.dateTime}</p>
            <p className="location">{props.venue}</p>
            {props.favourited ? (
                <button className="favourited-button" >Favourited</button>
            ) : (
                <button className="favourite-button" onClick={addedToFavourite}>Favourite</button>
            )}
        </div>
    )
}


export default Gig