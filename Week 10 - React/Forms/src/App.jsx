import Hello from "./components/Hello";
import makersLogo from "./assets/Makers-Logo.png";
import "./App.css";
import Form from "./components/form";
import { useState } from "react";


const TodoList = (props) => {
  const [todos, setTodos] = useState([]);

  const URL = `https://makers-todo-list-server.onrender.com/tagged/${props.tag}`;
  fetch(URL)
    .then((res) => res.json())
    .then((data) => setTodos(data));

  return (
    <>
      <h2>TODO List:</h2>
      <div className="todo-list">
        {todos.map((todoData) => (
          <Todo data={todoData} />
        ))}
      </div>
    </>
  );
};

function App() {
  return (
    <>
      <Hello name="World" />
      <img className="logo" src={makersLogo}></img>
      <Form />
      <TodoList 
      tag = '1'
      />
    </>
  );
}

export default App;
