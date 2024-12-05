import { Config } from '../..';
import { arraysEqual } from '../../aocutils';
import { calculateResult } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  return calculateResult(data, arraysEqual);
}

export const testResult = 143;
