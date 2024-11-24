import { Config } from '../..';
import { computeSumOfPotsWithPlants } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  return computeSumOfPotsWithPlants(data, 20);
}

export const testResult = 325;
