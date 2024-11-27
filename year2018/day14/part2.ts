import { Config } from '../..';
import { processRecipes } from './common';

function thresholdIndex(recipes: number[], threshold: number) {
  const lastRecipes = recipes.slice(-(threshold.toString().length + 1)).join('');
  return lastRecipes.indexOf(threshold.toString());
}

export async function run(data: string[], config: Config): Promise<string | number> {
  return processRecipes(
    data,
    (recipes, threshold) => thresholdIndex(recipes, threshold) >= 0,
    (recipes, threshold) =>
      recipes.length - threshold.toString().length - (1 - thresholdIndex(recipes, threshold)),
  );
}

export const testResult = 2018;
