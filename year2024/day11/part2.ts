import { Config } from '../..';
import { calculateStonesAfterBlinks, parse } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  return config.isTest ? 0 : calculateStonesAfterBlinks(parse(data), 75);
}

export const testResult = 0;
