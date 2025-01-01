import { Config } from '../..';
import { distance, nextPosition, parse, Point } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  let position: Point = [0, 0, 0];

  for (const direction of parse(data)) {
    position = nextPosition(position, direction);
  }

  return distance([0, 0, 0], position);
}

export const testResult = 3;
