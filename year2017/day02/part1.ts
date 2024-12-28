import { Config } from '../..';
import { sum } from '../../aocutils';
import { parse } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  return sum(parse(data).map((numbers) => Math.max(...numbers) - Math.min(...numbers)));
}

export const testResult = 18;
