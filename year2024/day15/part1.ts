import { Config } from '../..';
import { Matrix } from '../../aocutils';
import { Type, organizeWarehouse, parse, sumGpsCoordinates, merge } from './common';

function determineBoxesToMove(
  warehouse: Matrix<string>,
  robotPosition: [number, number],
  change: [number, number],
) {
  const boxes = [];

  let nextPosition: [number, number] = [robotPosition[0] + change[0], robotPosition[1] + change[1]];
  while (warehouse.get(...nextPosition) === Type.BOX) {
    boxes.push(nextPosition);
    nextPosition = merge(nextPosition, change);
  }

  if (warehouse.get(...nextPosition) !== Type.FREE) {
    return [];
  }

  return boxes;
}

export async function run(data: string[], config: Config): Promise<string | number> {
  const [warehouse, moves] = parse(data, config);
  await organizeWarehouse(warehouse, moves, determineBoxesToMove, config);
  return sumGpsCoordinates(warehouse, config);
}

export const testResult = 10092;
