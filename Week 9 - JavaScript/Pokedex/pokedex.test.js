const fetchPokemon = require("./api");

describe("Fetch a pokemon", () => {
  test("Get results for charizard", (done) => {
    fetchPokemon("Charizard").then((PokemonData) => {
      expect(PokemonData.id).toEqual(6);
      done();
    });
  });
});

const Pokedex = require("./pokedex");

describe("Test pokedex class", () => {
  test("Test initialises empty with all method", () => {
    const pokedex = new Pokedex();
    expect(pokedex.all()).toEqual([]);
  });

  test("Test can add pokemon", async () => {
    const pokedex = new Pokedex();
    await pokedex.catch("Charizard");

    expect(pokedex.all()).toEqual([
      {
        name: "charizard",
        id: 6,
        height: 17,
        weight: 905,
        types: ["fire", "flying"],
      },
    ]);
  });

  test("Test can add multiple pokemon", async () => {
    const pokedex = new Pokedex();
    await pokedex.catch("Charizard");
    await pokedex.catch("Bulbasaur");

    expect(pokedex.all()).toEqual([
      {
        name: "charizard",
        id: 6,
        height: 17,
        weight: 905,
        types: ["fire", "flying"],
      },
      {
        name: "bulbasaur",
        id: 1,
        height: 7,
        weight: 69,
        types: ["grass", "poison"],
      },
    ]);
  });
});
