import { Config } from '../..';

export async function run(data: string[], config: Config): Promise<string | number> {
  const pattern = /mul\((\d{1,3}),(\d{1,3})\)|don't\(\)|do\(\)/g;

  let sum = 0;
  let counting = true;

  for (const line of data) {
    for (const [m, a, b] of line.matchAll(pattern)) {
      if (m === "don't()") {
        counting = false;
      } else if (m === 'do()') {
        counting = true;
      } else if (counting) {
        sum += parseInt(a) * parseInt(b);
      }
    }
  }

  return sum;
}

export const testResult = 48;
