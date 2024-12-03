import { Config } from '../..';
import { Matrix } from '../../aocutils';
import { manhattan, parse, Point } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const points = parse(data);
  const size = config.isTest ? 15 : 1000;
  const space = Matrix.create(size, size, 0);

  let result = 0;
  for (const [row, col] of space.positions()) {
    const point1 = { id: 0, row, col };
    const sumOfDistances = points.reduce((sum, point2) => sum + manhattan(point1, point2), 0);
    if (sumOfDistances < (config.isTest ? 32 : 10000)) {
      result++;
    }
  }

  return result;
}

export const testResult = 16;
