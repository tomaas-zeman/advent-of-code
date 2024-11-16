import { manhattan, parse, Point } from './common';
import m from 'ml-matrix';

export function run(data: string[], isTest?: boolean): string | number {
  const points = parse(data);
  const space = isTest ? m.zeros(15, 15) : m.zeros(1000, 1000);

  for (let row = 0; row < space.rows; row++) {
    for (let col = 0; col < space.columns; col++) {
      const pointsByDistance = points
        .map<[Point, number]>((p) => [p, manhattan(new Point(0, row, col), p)])
        .sort(([p1, dist1], [p2, dist2]) => dist1 - dist2);
      const shortestDistance = pointsByDistance[0][1];
      const closestPoints = pointsByDistance.filter(([p, dist]) => dist === shortestDistance);

      if (closestPoints.length === 1) {
        space.set(row, col, pointsByDistance[0][0].id);
      }
    }
  }

  const infinitePoints = new Set([
    ...space.getRow(0),
    ...space.getRow(space.rows - 1),
    ...space.getColumn(0),
    ...space.getColumn(space.columns - 1),
  ]);

  const counter: { [id: number]: number } = {};
  for (let value of space.values()) {
    if (infinitePoints.has(value)) {
      continue;
    }
    if (!counter[value]) {
      counter[value] = 0;
    }
    counter[value]++;
  }

  return Math.max(...Object.values(counter));
}

export const testResult = 17;
