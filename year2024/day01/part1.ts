import zipWith from 'lodash/zipWith';
import { Config } from '../..';
import { sum } from '../../aocutils';
import { parseInput } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const [list1, list2] = parseInput(data);
  return sum(zipWith(list1.sort(), list2.sort(), (a, b) => Math.abs(a - b)));
}

export const testResult = 11;
