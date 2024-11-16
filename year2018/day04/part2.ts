import { parse } from './common';

export function run(data: string[]): string | number {
  const guards = parse(data);
  const guardWithMaxOverlap = Object.values(guards).sort(
    (g1, g2) => g2.getMaxOverlap() - g1.getMaxOverlap(),
  )[0];
  return guardWithMaxOverlap.getMinuteOfMaxOverlap() * guardWithMaxOverlap.id;
}

export const testResult = 4455;
