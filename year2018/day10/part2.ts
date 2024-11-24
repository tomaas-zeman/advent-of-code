import { Config } from '../..';
import { run as runPart1 } from './part1';

export async function run(data: string[], config: Config) {
  return runPart1(data, config);
}

export const testResult = 0;
