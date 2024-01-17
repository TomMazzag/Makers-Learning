const phoneNumbers = () => {
  const checkLength = (phonenumber) => {
    if (phonenumber.length <= 10) {
      return true;
    } else {
      return false;
    }
  };

  const filterLongNumbers = (phonenumbers) => {
    const filteredNumbers = phonenumbers.filter(checkLength);
    return filteredNumbers;
  };

  const numbers = [
    "1763687364",
    "4763687363",
    "7867867862",
    "aaaaaaaabbbbbbbcccccdddddddd",
  ];

  console.log(filterLongNumbers(numbers));
  console.log(filterLongNumbers([]));
};

const personalisedMessages = () => {
  const names = ["Anna", "Laura", "Josh", "Min", "Karla"];

  const generateMessage = (nameList) => {
    return nameList.map((name) => {
      return `Hi ${name}! 50% off our best cookies for you today!`;
    });
  };

  return generateMessage(names);
};

const challenge = () => {
  const namesAndDiscounts = [
    { name: "Anna", discount: 50 },
    { name: "Laura", discount: 40 },
    { name: "Josh", discount: 30 },
    { name: "Min", discount: 50 },
    { name: "Karla", discount: 60 },
  ];

  const generateMessage = (nameAndDiscountList) => {
    return nameAndDiscountList.map(({ name, discount }) => {
      return `Hi ${name}! ${discount}% off our best cookies for you today!`;
    });
  };

  return generateMessage(namesAndDiscounts);
};

console.log(challenge());
