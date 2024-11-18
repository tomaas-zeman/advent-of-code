import { Config } from '../..';
import { parse } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const guards = parse(data);
  const guardWithMaxOverlap = Object.values(guards).sort(
    (g1, g2) => g2.getMaxOverlap() - g1.getMaxOverlap(),
  )[0];
  return guardWithMaxOverlap.getMinuteOfMaxOverlap() * guardWithMaxOverlap.id;
}

export const testResult = 4455;
