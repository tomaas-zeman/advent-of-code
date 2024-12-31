import { Config } from '../..';
import { getResult } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  return getResult(data, (offset) => (offset >= 3 ? -1 : 1));
}

export const testResult = 10;
