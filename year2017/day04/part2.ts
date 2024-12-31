import { Combination } from 'js-combinatorics';
import { Config } from '../..';
import { isEqual } from '../../aocutils';

export async function run(data: string[], config: Config): Promise<string | number> {
  let valid = 0;

  for (const words of data.map(line => line.split(' '))) {
    let isValid = true;
    for (const [a, b] of new Combination(words, 2)) {
      if (isEqual(a.split('').sort(), b.split('').sort())) {
        isValid = false;
        break;
      }
    }
    if (isValid) {
      valid++;
    }
  }

  return valid;
}

export const testResult = 2;
