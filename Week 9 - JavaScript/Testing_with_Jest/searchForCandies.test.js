const candies = [
  { name: "Aero", price: 1.99 },
  { name: "Skitties", price: 2.99 },
  { name: "Mars", price: 1.49 },
  { name: "Maltesers", price: 3.49 },
  { name: "Skittles", price: 1.49 },
  { name: "Starburst", price: 5.99 },
  { name: "Ricola", price: 1.99 },
  { name: "Polkagris", price: 5.99 },
  { name: "Pastila", price: 4.99 },
  { name: "Mentos", price: 8.99 },
  { name: "Raffaello", price: 7.99 },
  { name: "Gummi bears", price: 10.99 },
  { name: "Fraise Tagada", price: 5.99 },
];

const searchCandies = (SearchString, MaxPrice) => {
  meetsSearchCriteria = candies.filter(
    ({ name, price }) => name.startsWith(SearchString) && price < MaxPrice
  );
  return meetsSearchCriteria.map(({ name }) => {
    return name;
  });
};

describe("Tests", () => {
  it("Test the search function (Ma, 10)", () => {
    expect(searchCandies("Ma", 10)).toEqual(["Mars", "Maltesers"]);
  });

  it("Test the search function (Ma, 2)", () => {
    expect(searchCandies("Ma", 2)).toEqual(["Mars"]);
  });

  it("Test the search function (S, 10)", () => {
    expect(searchCandies("S", 10)).toEqual([
      "Skitties",
      "Skittles",
      "Starburst",
    ]);
  });

  it("Test the search function (S, 4)", () => {
    expect(searchCandies("S", 4)).toEqual(["Skitties", "Skittles"]);
  });
});
