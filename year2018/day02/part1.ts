import countBy from 'lodash/countBy';
import { Config } from '../..';

export async function run(data: string[], config: Config): Promise<string | number> {
  const counts = data.map((word) => countBy(word.split('')));
  const twos = counts.filter((count) => Object.values(count).includes(2)).length;
  const threes = counts.filter((count) => Object.values(count).includes(3)).length;
  return twos * threes;
}

export const testResult = 12;
