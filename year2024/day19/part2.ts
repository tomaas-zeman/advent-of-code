import { Config } from '../..';
import { sum } from '../../aocutils';
import { countValidCombinations, parse } from './commons';

export async function run(data: string[], config: Config): Promise<string | number> {
  const [towels, designs] = parse(data);
  return sum(designs.map(countValidCombinations(towels)));
}

export const testResult = 16;
