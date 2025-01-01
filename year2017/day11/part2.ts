import { Config } from '../..';
import { distance, nextPosition, parse, Point } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  let maxDistance = 0;
  let position: Point = [0, 0, 0];

  for (const direction of parse(data)) {
    position = nextPosition(position, direction);
    maxDistance = Math.max(maxDistance, distance([0, 0, 0], position));
  }

  return maxDistance;
}

export const testResult = 3;
