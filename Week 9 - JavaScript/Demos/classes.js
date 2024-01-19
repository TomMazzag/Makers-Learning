const example = () => {
  class Rectange {
    constructor(height, width) {
      this.height = height;
      this.width = width;
    }

    getArea() {
      return this.height * this.width;
    }
  }

  const rect = new Rectange(3, 5);
  console.log(rect.getArea());
};

const excersies = () => {
  class User {
    constructor(name) {
      this.name = name;
    }

    getName() {
      return this.name;
    }

    getIntroduction() {
      return "Hi, my name is " + this.name;
    }
  }

  class UserBase {
    constructor(names) {
      this.names = names;
    }

    count() {
      return this.names.length;
    }

    getNames() {
      return this.names.map((user) => user.getName());
    }

    getIntroductions() {
      return this.names.map((user) => user.getIntroduction());
    }
  }

  const users = [new User("Uma"), new User("Josh"), new User("Ollie")];
  const userBase = new UserBase(users);

  console.log(userBase.count());
  console.log(userBase.getNames());
  console.log(userBase.getIntroductions());
};

const challenge = () => {
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

  module.exports = Candy;

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

  const candy = new Candy("Mars", 4.99);

  //console.log(candy.getName());
  //console.log(candy.getPrice());

  const basket = new ShoppingBasket();

  basket.addItem(candy);

  basket.addItem(new Candy("Skittle", 3.99));
  basket.addItem(new Candy("Skittle", 3.99));

  console.log(basket.getTotalPrice());
};
