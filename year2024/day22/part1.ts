import { Config } from '../..';
import { sum } from '../../aocutils';
import { getSecretNumbers } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  return sum(data.asInt().map((n) => getSecretNumbers(n).get(-1)));
}

export const testResult = 37327623;
