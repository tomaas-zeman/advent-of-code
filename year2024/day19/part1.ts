import { Config } from '../..';
import { countValidCombinations, parse } from './commons';

export async function run(data: string[], config: Config): Promise<string | number> {
  const [towels, designs] = parse(data);
  const combinations = designs.map(countValidCombinations(towels));
  return combinations.filter((c) => c > 0).length;
}

export const testResult = 6;
