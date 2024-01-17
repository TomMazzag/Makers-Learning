const example = () => {
  const person = {
    name: "Maxine",
    age: 32,
    address: {
      city: "London",
      postcode: "E1 123",
    },
    hobbies: ["writing", "tennis", "cooking"],
  };

  console.log(person.address.city);
  console.log(person.hobbies[1]);
};

const cohort = {
  name: "May2022",
  id: "1234",
  students: ["Tom", "Ben", "Maxine"],
};

const logCohortDetails = (cohort) => {
  return `${cohort.id} - ${cohort.name} - ${cohort.students.length} students in this cohort`;
};

console.log(logCohortDetails(cohort));
