const body = document.querySelector("body");
const button = document.querySelector("button");

const todoList = document.createElement("ol");

button.addEventListener("click", () => {
  todoTask = Math.floor(Math.random() * 20) + 1;
  console.log(todoTask);
  fetch(`https://jsonplaceholder.typicode.com/todos/${todoTask}`)
    .then((response) => response.json())
    .then((todo) => {
      const nextTask = document.createElement("li");
      nextTask.innerText = todo.title;
      todoList.appendChild(nextTask);

      body.appendChild(todoList);
    });
});
