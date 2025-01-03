import { Config } from '../..';

export async function run(data: string[], config: Config): Promise<string | number> {
  const step = parseInt(data[0]);

  const mem = [0];
  let position = 0;

  for (let n = 1; n <= 2017; n++) {
    position = ((position + step) % mem.length) + 1;
    mem.splice(position, 0, n);
  }

  return mem[position + 1];
}

export const testResult = 638;
