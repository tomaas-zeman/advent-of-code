import isEqual from 'lodash/isEqual';
import { Config } from '../..';
import { calculateResult } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  return calculateResult(data, (a, b) => !isEqual(a, b));
}

export const testResult = 123;
