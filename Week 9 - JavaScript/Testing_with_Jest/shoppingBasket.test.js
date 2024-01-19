class ShoppingBasket {
  constructor(basket = []) {
    this.basket = basket;
    this.total = 0;
  }

  getTotalPrice() {
    this.basket.forEach(({ price }) => (this.total += price));
    return this.total;
  }

  addItem(candy) {
    this.basket.push(candy);
  }
}

describe("Unit tests for shopping basket class", () => {
  it("Test add item", () => {
    const candy = {
      name: "Mars",
      price: 4.99,
    };

    const basket = new ShoppingBasket();
    basket.addItem(candy);

    expect(basket.basket).toEqual([{ name: "Mars", price: 4.99 }]);
  });

  it("Test get total", () => {
    const candy = {
      name: "Mars",
      price: 4.99,
    };

    const basket = new ShoppingBasket();
    basket.addItem(candy);

    expect(basket.getTotalPrice()).toEqual(4.99);
  });
});
