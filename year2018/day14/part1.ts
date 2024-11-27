import { Config } from '../..';
import { processRecipes } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  return processRecipes(
    data,
    (recipes, threshold) => recipes.length >= threshold + 10,
    (recipes, threshold) => recipes.slice(threshold, threshold + 10).join(''),
  );
}

export const testResult = '5941429882';
