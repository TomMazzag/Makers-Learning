import { useState } from "react";

const Form = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const handleUsernameChange = (event) => {
        const userInput = (event.target.value);
        setUsername(userInput)
    };

    const handlePasswordChange = (event) => {
        const userInput = (event.target.value);
        setPassword(userInput)
    };

    const handleSubmit = (event) => {
        event.preventDefault()

        console.log(username, password)

        fetch('http://url.com/endpoint'), {
            method: "POST",
            body: JSON.stringify({ username: username })
        }
    }

    return (
      <form onSubmit={handleSubmit}>
        <label>
          Enter your username:
          <input type="username" name="username" value={username} onChange={handleUsernameChange} required/>
        </label>
        <label>
          Enter your password:
          <input type="password" name="password" value={password} onChange={handlePasswordChange} required/>
        </label>
        <label>
            Submit
            <input type="submit" name="submit" />
        </label>
      </form>
    );
  };

export default Form