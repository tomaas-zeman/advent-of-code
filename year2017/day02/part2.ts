import { Combination } from 'js-combinatorics';
import { Config } from '../..';
import { parse } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  let checksum = 0;

  for (const numbers of parse(data)) {
    for (const pair of new Combination(numbers, 2)) {
      const div = Math.max(...pair) / Math.min(...pair);
      if (div % 1 === 0) {
        checksum += div;
      }
    }
  }

  return checksum;
}

export const testResult = 9;
