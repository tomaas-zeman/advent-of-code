import { Config } from '../..';
import { parse } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const guards = parse(data);
  const guardWithMaxSleepTime = Object.values(guards).sort(
    (g1, g2) => g2.totalSleepTime - g1.totalSleepTime,
  )[0];
  return guardWithMaxSleepTime.getMinuteOfMaxOverlap() * guardWithMaxSleepTime.id;
}

export const testResult = 240;
