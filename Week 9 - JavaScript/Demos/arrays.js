const getTotal = () => {
  const nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

  total = 0;
  nums.forEach((amount) => (total += amount));
  console.log(total);
};

const addToBatch = (inputArray, numberToAdd) => {
  if (inputArray.length >= 5) {
    return inputArray;
  } else {
    newArray = inputArray.concat(numberToAdd);
    return newArray;
  }
};

console.log(addToBatch([1, 2, 3], 4));
console.log(addToBatch([], 8));
console.log(addToBatch([1, 2, 3, 4, 5, 6], 7));
console.log(addToBatch([1, 2, 3, 4, 5, 6, 7, 8, 9], 10));
