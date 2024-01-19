const Pokedex = require("./pokedex");

const pokedexTest = async () => {
  const pokedex = new Pokedex();
  await pokedex.catch("Charizard");
  await pokedex.catch("Bulbasaur");
  await pokedex.catch("Charmander");
  console.log(pokedex.all());
};

pokedexTest();
