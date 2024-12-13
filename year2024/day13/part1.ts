import { Config } from '../..';
import { calculateCost } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  return calculateCost(data, 0);
}

export const testResult = 480;
