import { Config } from '../..';
import { sum } from '../../aocutils';
import { constructBridges } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const bridges = constructBridges(data);
  const longestBridge = Math.max(...bridges.map((b) => b.length));
  return Math.max(
    ...bridges.filter((b) => b.length === longestBridge).map((b) => sum(b.flatMap((c) => c))),
  );
}

export const testResult = 19;
