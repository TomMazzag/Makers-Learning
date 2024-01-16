const notifyByEmail = (emailAddress) => {
  return `Email sent to: ${emailAddress}`;
};

const notifyByText = (phoneNumber) => {
  return `Text sent to: ${phoneNumber}`;
};

const notify = (emailOrPhone, functionToComplete) => {
  return functionToComplete(emailOrPhone);
};

console.log(notify("12345 678910", notifyByText));
console.log(notify("test@email.com", notifyByEmail));
