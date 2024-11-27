export function processRecipes(
  data: string[],
  resultCondition: (recipes: number[], threshold: number) => boolean,
  resultExtractor: (recipes: number[], threshold: number) => string | number,
) {
  const threshold = parseInt(data[0]);
  const recipes = [3, 7];
  const currentRecipesIndexes = [0, 1];

  while (true) {
    const newRecipes = (recipes[currentRecipesIndexes[0]] + recipes[currentRecipesIndexes[1]])
      .toString()
      .split('')
      .map((val) => parseInt(val));

    recipes.push(...newRecipes);

    if (resultCondition(recipes, threshold)) {
      return resultExtractor(recipes, threshold);
    }

    for (let i = 0; i < currentRecipesIndexes.length; i++) {
      const newIndex =
        (currentRecipesIndexes[i] + recipes[currentRecipesIndexes[i]] + 1) % recipes.length;
      currentRecipesIndexes[i] = newIndex;
    }
  }
}
