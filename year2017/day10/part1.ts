import range from 'lodash/range';
import { Config } from '../..';
import { runKnotHash } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const lengths = data[0].split(',').asInt();
  const numbers = range(0, config.isTest ? 5 : 256);
  
  runKnotHash(lengths, numbers, 1);
  return numbers[0] * numbers[1];
}

export const testResult = 12;
