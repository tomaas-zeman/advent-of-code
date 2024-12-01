import { Config } from '../..';
import { sum, zip } from '../../aocutils';
import { parseInput } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const [list1, list2] = parseInput(data);
  return sum(zip(list1.sort(), list2.sort(), (a, b) => Math.abs(a - b)));
}

export const testResult = 11;
