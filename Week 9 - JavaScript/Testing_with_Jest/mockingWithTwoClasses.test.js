describe("Unit Tests", () => {
  it("Test Mock candy", () => {
    const candy = {
      name: "Mars",
      price: 4.99,
      getName: () => {
        return candy.name;
      },
    };

    expect(candy.getName()).toEqual("Mars");
  });
});
