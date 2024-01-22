const body = document.querySelector("body");
const title = document.createElement("h1");
const punchline = document.createElement("p");

const button = document.createElement("button");
button.textContent = "Reveal Joke";

fetch("https://official-joke-api.appspot.com/random_joke")
  .then((response) => response.json())
  .then((joke) => {
    title.textContent = joke.setup;
    punchline.textContent = joke.punchline;
    body.appendChild(title);
    body.appendChild(button);
  });

button.addEventListener("click", () => {
  body.appendChild(punchline);
});
