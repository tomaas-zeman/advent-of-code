import { Config } from '../..';
import { calculateTrailheadRatings, Point } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  return calculateTrailheadRatings(data, (path: Point[]) => path);
}

export const testResult = 81;
