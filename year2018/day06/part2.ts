import { Config } from '../..';
import { manhattan, Matrix } from '../../aocutils';
import { parse } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const points = parse(data);
  const size = config.isTest ? 15 : 1000;
  const space = Matrix.create(size, size, 0);

  let result = 0;
  for (const p1 of space.positions()) {
    const sumOfDistances = points.reduce((sum, p2) => sum + manhattan(p1, [p2.row, p2.col]), 0);
    if (sumOfDistances < (config.isTest ? 32 : 10000)) {
      result++;
    }
  }

  return result;
}

export const testResult = 16;
