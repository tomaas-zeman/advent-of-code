import { Config } from '../..';
import { redistribute } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const [steps] = redistribute(data);
  return steps;
}

export const testResult = 5;
