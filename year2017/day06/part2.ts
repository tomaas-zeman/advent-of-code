import { Config } from '../..';
import { redistribute } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const [steps, blocks, states] = redistribute(data);
  return steps - states.get(blocks);
}

export const testResult = 4;
