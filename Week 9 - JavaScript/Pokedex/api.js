const fetchPokemon = (pokemon) => {
  PokemonData = [];
  fetch("https://pokeapi.co/api/v2/pokemon/" + pokemon.toLowerCase())
    .then((response) => response.json())
    .then((data) =>
      console.log(
        (PokemonData = {
          name: data.name,
          id: data.id,
          height: data.height,
          weight: data.weight,
          types: data.types.map((type) => type.type.name),
        })
      )
    );
};

const fetchPokemonAsync = async (pokemon) => {
  const response = await fetch(
    "https://pokeapi.co/api/v2/pokemon/" + pokemon.toLowerCase()
  );
  const data = await response.json();

  PokemonData = {
    name: data.name,
    id: data.id,
    height: data.height,
    weight: data.weight,
    types: data.types.map((type) => type.type.name),
  };

  return PokemonData;
};

module.exports = fetchPokemonAsync;
