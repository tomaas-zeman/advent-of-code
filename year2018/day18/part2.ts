import { Config } from '../..';
import { calculateResourceValue } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  return calculateResourceValue(data, 1000000000);
}

export const testResult = 0;
