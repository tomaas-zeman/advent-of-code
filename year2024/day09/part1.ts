import { Config } from '../..';
import { computeCheckSum, parse } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const [fs] = parse(data);

  let left = 0;
  let right = fs.length - 1;

  while (left < right) {
    while (fs[left] != null) {
      left++;
    }
    while (fs[right] == null) {
      right--;
    }

    fs[left] = fs[right];
    fs[right] = null;
    left++;
    right--;
  }

  return computeCheckSum(fs.filter((v) => v != null));
}

export const testResult = 1928;
