import { Config } from '../..';
import { Point3D } from '../../aocutils';
import { distance, nextPosition, parse } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  let position: Point3D = [0, 0, 0];

  for (const direction of parse(data)) {
    position = nextPosition(position, direction);
  }

  return distance([0, 0, 0], position);
}

export const testResult = 3;
