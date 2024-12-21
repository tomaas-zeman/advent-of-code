import { Config } from '../..';
import { isEqual } from '../../aocutils';
import { calculateResult } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  return calculateResult(data, isEqual);
}

export const testResult = 143;
