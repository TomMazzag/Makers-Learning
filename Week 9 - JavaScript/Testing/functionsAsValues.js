const doubleNumber = (n) => 2 * n;

const simpleCalculation = doubleNumber;

console.log(simpleCalculation(2));

const uppercaseMessage = (message) => {
  return message.toUpperCase();
};

// This function accepts as arguments a string message, and a function.
// It then calls the given function to do its job.
const transform = (message, transformFunction) => {
  return transformFunction(message);
};

console.log(transform("hello", uppercaseMessage));
