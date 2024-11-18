import { Config } from '../..';
import { parse } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const [pointOverlaps, claims] = parse(data);
  for (let claim of claims) {
    if (claim.points().every((point) => pointOverlaps[point.hash()] === 1)) {
      return claim.id;
    }
  }

  throw new Error('There is no claim that does not have an overlap.');
}

export const testResult = 3;
