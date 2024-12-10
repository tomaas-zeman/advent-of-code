import countBy from 'lodash/countBy';
import { Config } from '../..';
import { Matrix } from '../../aocutils';
import { manhattan, parse, Point } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const points = parse(data);
  const size = config.isTest ? 15 : 1000;
  const space = Matrix.create(size, size, 0);

  for (const [row, col] of space.positions()) {
    const pointsByDistance = points
      .map<[Point, number]>((p) => [p, manhattan({ id: 0, row, col }, p)])
      .sort(([_, dist1], [__, dist2]) => dist1 - dist2);
    const shortestDistance = pointsByDistance[0][1];
    const closestPoints = pointsByDistance.filter(([p, dist]) => dist === shortestDistance);

    if (closestPoints.length === 1) {
      space.set(row, col, pointsByDistance[0][0].id);
    }
  }

  const infinitePoints = new Set([
    ...space.row(0),
    ...space.row(space.rows - 1),
    ...space.column(0),
    ...space.column(space.cols - 1),
  ]);

  const counts = countBy([...space.values()].filter((value) => !infinitePoints.has(value)));
  return Math.max(...Object.values(counts));
}

export const testResult = 17;
