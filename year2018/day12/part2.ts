import { Config } from '../..';
import { computeSumOfPotsWithPlants } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  return computeSumOfPotsWithPlants(data, 50000000000);
}

export const testResult = 999999999374;
