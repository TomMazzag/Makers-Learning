const sayHi = require("../Demos/sayHello");

describe("First tests", () => {
  it("This is the test itself, say hi name", () => {
    expect(sayHi("Tom")).toBe("Hello Tom!");
  });

  it("TestBuzz", () => {
    let fizzBuzz = require("../Demos/fizzBuzz");
    expect(fizzBuzz("5")).toBe("Buzz");
  });

  it("TestFizz", () => {
    let fizzBuzz = require("../Demos/fizzBuzz");
    expect(fizzBuzz("3")).toBe("Fizz");
  });

  it("FizzBuzz returns number", () => {
    let fizzBuzz = require("../Demos/fizzBuzz");
    expect(fizzBuzz("7")).toBe("7");
  });
});
