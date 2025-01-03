import { Config } from '../..';
import { createGenerator, factorA, factorB, countMatches, parse } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const [valueA, valueB] = parse(data);
  const genA = createGenerator(valueA, factorA, 4n);
  const genB = createGenerator(valueB, factorB, 8n);
  return countMatches(genA, genB, 5_000_000);
}

export const testResult = 309;
