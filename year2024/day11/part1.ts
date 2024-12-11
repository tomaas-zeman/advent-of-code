import { Config } from '../..';
import { calculateStonesAfterBlinks, parse } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  return calculateStonesAfterBlinks(parse(data), 25);
}

export const testResult = 55312;
