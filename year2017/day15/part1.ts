import { Config } from '../..';
import { countMatches, createGenerator, factorA, factorB, parse } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const [valueA, valueB] = parse(data);
  const genA = createGenerator(valueA, factorA, 1n);
  const genB = createGenerator(valueB, factorB, 1n);
  return countMatches(genA, genB, 40_000_000);
}

export const testResult = 588;
