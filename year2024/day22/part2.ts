import range from 'lodash/range';
import { Config } from '../..';
import { DefaultMap, pairwise, sum } from '../../aocutils';
import { getSecretNumbers, STEPS } from './common';

function processNumbers(numbers: number[], step: number): [any, any] {
  const lastDigits = numbers.slice(step, step + 5).map((n) => n % 10);
  const pattern = pairwise(lastDigits, 2).map(([a, b]) => b - a).join(',');
  const bananas = lastDigits.get(-1);
  return [pattern, bananas];
}

export async function run(data: string[], config: Config): Promise<string | number> {
  const numbers = data.asInt().map(getSecretNumbers);
  const result = new DefaultMap<string, number[]>(() => new Array(numbers.length).fill(0));

  for (let buyer = 0; buyer < numbers.length; buyer++) {
    for (let i = 0; i < numbers[0].length - 4; i++) {
      const [pattern, bananas] = processNumbers(numbers[buyer], i);
      if (result.get(pattern)[buyer] === 0) {
        result.get(pattern)[buyer] = bananas;
      }
    }
  }

  return Math.max(...result.values().map((v) => sum(v)));
}

export const testResult = 23;
