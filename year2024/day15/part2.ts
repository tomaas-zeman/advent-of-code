import { Config } from '../..';
import { Matrix } from '../../aocutils';
import { organizeWarehouse, parse, sumGpsCoordinates, Type } from './common';


function getWholeBox(warehouse: Matrix<string>, part: [number, number]): [number, number][] {
  if (warehouse.get(...part) === Type.BOX_L) {
    return [part, [part[0], part[1] + 1]];
  }
  if (warehouse.get(...part) === Type.BOX_R) {
    return [[part[0], part[1] - 1], part];
  }
  return [];
}

function determineBoxesToMove(
  warehouse: Matrix<string>,
  robotPosition: [number, number],
  change: [number, number],
): [number, number][] {
  const boxes: [number, number][] = [];
  const queue: [number, number][] = [robotPosition];

  while (queue.length > 0) {
    const currentPos = queue.shift()!;
    const nextPos: [number, number] = [currentPos[0] + change[0], currentPos[1] + change[1]];
    const nextVal = warehouse.get(...nextPos);

    if (nextVal === Type.WALL) {
      return [];
    }
    if (nextVal === Type.FREE) {
      continue;
    }

    const box = getWholeBox(warehouse, nextPos);
    if (!boxes.find(([row, col]) => row === box[0][0] && col === box[0][1])) {
      boxes.push(...box);
    }
    
    if (change[0] !== 0) { // up/down
      queue.push(...box);
    } else if (change[1] === -1) { // left
      queue.push(box[0]);
    } else if (change[1] === 1) { // right
      queue.push(box[1]);
    }
  }

  return boxes
}

export async function run(data: string[], config: Config): Promise<string | number> {
  const [warehouse, moves] = parse(data, config);
  organizeWarehouse(warehouse, moves, determineBoxesToMove);
  return sumGpsCoordinates(warehouse, config);
}

export const testResult = 9021;
