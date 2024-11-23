import { Config } from '../..';
import { computeScores, parseData } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  return computeScores(...parseData(data));
}

export const testResult = 8317;
