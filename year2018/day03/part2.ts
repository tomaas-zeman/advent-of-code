import { parse } from './common';

export function run(data: string[]): string | number {
  const [pointOverlaps, claims] = parse(data);
  for (let claim of claims) {
    if (claim.points().every((point) => pointOverlaps[point.hash()] === 1)) {
      return claim.id;
    }
  }

  throw new Error('There is no claim that does not have an overlap.');
}

export const testResult = 3;
