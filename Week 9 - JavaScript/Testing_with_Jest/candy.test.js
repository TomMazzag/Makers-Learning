class Candy {
  constructor(name, price) {
    this.name = name;
    this.price = price;
  }

  getName() {
    return this.name;
  }

  getPrice() {
    return this.price;
  }
}

describe("Unit Test for Candy class", () => {
  it("Test getName method", () => {
    const candy = new Candy("Mars", 4.99);
    expect(candy.getName()).toBe("Mars");
  });
  it("Test getPrice method", () => {
    const candy = new Candy("Mars", 4.99);
    expect(candy.getPrice()).toBe(4.99);
  });
});
