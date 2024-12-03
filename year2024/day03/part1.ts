import { Config } from '../..';

export async function run(data: string[], config: Config): Promise<string | number> {
  const pattern = /mul\((\d{1,3}),(\d{1,3})\)/g;
  
  let sum = 0;

  for (const line of data) {
    for (const [_, a, b] of line.matchAll(pattern)) {
      sum += parseInt(a) * parseInt(b);
    }
  }

  return sum;
}

export const testResult = 161;
