const isValidLength = (phoneNumber) => {
  const validLength = 11;
  if (phoneNumber.length === validLength) {
    return true;
  } else {
    return false;
  }
};

console.log("Check if 00 is valid", isValidLength("00"));
console.log("Check if 00112233445 is valid", isValidLength("00112233445"));
