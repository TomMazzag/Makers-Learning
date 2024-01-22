import './gig.css'

const Gig = (props) => {
    const bandName = 'Nothing But Thieves'
    return (
        <div className="gig">
           <h3 className="bandName">{props.band}</h3>
            <img src={props.imageURL} alt="" className="bandImage"/> 
            <p className="eventDescription">{props.description}</p>
            <p className="dateTime">{props.dateTime}</p>
            <p className="location">{props.venue}</p>
        </div>
    )
}

/* 
<div className="gig">
           <h3 className="bandName">{bandName}</h3>
            <img src="../src/assets/nbt.webp" alt="" className="bandImage"/> 
            <p className="eventDescription">Come see {bandName} at Wembley Arena!</p>
            <p className="dateTime">20/02/24 20:00</p>
            <p className="location">OVO Wembley</p>
        </div>
*/

export default Gig