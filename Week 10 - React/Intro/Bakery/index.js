const addRecipe = (PageTile, steps) => {
  document.querySelector(
    "p"
  ).textContent = `Check out my latest breakfast recipe for ${PageTile}!`;

  const body = document.querySelector("body");
  const recipeListEl = document.createElement("ol"); // Create a unordered list element

  steps.map((step) => {
    const nextStep = document.createElement("li");
    nextStep.innerText = step;
    recipeListEl.appendChild(nextStep);
  });

  body.appendChild(recipeListEl); // Add the recipe list onto the body of the page
};

addRecipe("Toast", [
  "Toast some bread",
  "Spread butter on the toast",
  "All done",
]);
