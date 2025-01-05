import { Config } from '../..';
import { sum } from '../../aocutils';
import { constructBridges } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const bridges = constructBridges(data);
  return Math.max(...bridges.map((b) => sum(b.flatMap((c) => c))));
}

export const testResult = 31;
