const fetchPokemonAsync = require("./api");

class Pokedex {
  constructor() {
    this.pokedex = [];
  }

  catch(pokemon) {
    return fetchPokemonAsync(pokemon).then((PokemonData) => {
      this.pokedex.push(PokemonData);
    });
  }

  all() {
    return this.pokedex;
  }
}

module.exports = Pokedex;
