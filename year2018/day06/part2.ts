import { manhattan, parse, Point } from './common';
import * as m from 'mathjs';

export function run(data: string[], isTest?: boolean): string | number {
  const points = parse(data);
  const space = m.matrix(isTest ? m.zeros(15, 15) : m.zeros(1000, 1000));

  let result = 0;
  for (let row = 0; row < space.size()[0]; row++) {
    for (let col = 0; col < space.size()[1]; col++) {
      const point1 = new Point(0, row, col);
      const sumOfDistances = points.reduce((sum, point2) => sum + manhattan(point1, point2), 0);
      if (sumOfDistances < (isTest ? 32 : 10000)) {
        result++;
      }
    }
  }

  return result;
}

export const testResult = 16;
