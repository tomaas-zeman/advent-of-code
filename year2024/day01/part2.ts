import { Config } from '../..';
import { counter } from '../../aocutils';
import { parseInput } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const [list1, list2] = parseInput(data);
  const list2Counts = counter(list2);
  return list1.reduce((sum, n) => sum + n * (list2Counts[n] || 0), 0);
}

export const testResult = 31;
