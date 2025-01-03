import { Config } from '../..';

export async function run(data: string[], config: Config): Promise<string | number> {
  const step = parseInt(data[0]);

  let result = 0;
  let position = 0;

  for (let n = 1; n <= 50_000_000; n++) {
    position = ((position + step) % n) + 1;

    if (position === 1) {
      result = n;
    }
  }

  return result;
}

export const testResult = 1222153;
