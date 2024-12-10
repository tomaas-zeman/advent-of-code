import { Config } from '../..';
import { calculateTrailheadRatings, Point } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const hash = (path: Point[]) => path.map((point) => point.join(':')).join('>');
  return calculateTrailheadRatings(data, hash);
}

export const testResult = 81;
