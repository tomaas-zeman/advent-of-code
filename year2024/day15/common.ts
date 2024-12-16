import { Config } from '../..';
import { Matrix, MatrixAnimation } from '../../aocutils';

export enum Type {
  ROBOT = '@',
  BOX = 'O',
  WALL = '#',
  FREE = '.',
  BOX_L = '[',
  BOX_R = ']',
}

const changes: { [move: string]: [number, number] } = {
  '<': [0, -1],
  '>': [0, 1],
  '^': [-1, 0],
  v: [1, 0],
};

function expandSpace(line: string) {
  return line
    .replaceAll('#', '##')
    .replaceAll('O', '[]')
    .replaceAll('.', '..')
    .replaceAll('@', '@.');
}

export function parse(data: string[], config: Config): [Matrix<string>, string[]] {
  const splitIndex = data.findIndex((v) => !v);
  const preprocessedData = data.map((line) => (config.part === '2' ? expandSpace(line) : line));
  const matrixData = preprocessedData.slice(0, splitIndex).map((row) => row.split(''));
  const warehouse = new Matrix<string>(matrixData).pad(1, '#');
  const moves = data
    .slice(splitIndex + 1)
    .join('')
    .split('');

  return [warehouse, moves];
}

export function sumGpsCoordinates(warehouse: Matrix<string>, config: Config): number {
  return warehouse
    .findAll(config.part === '1' ? Type.BOX : Type.BOX_L)
    .reduce((sum, [row, col]) => sum + 100 * (row - 1) + (col - 1), 0);
}

export function merge(position: [number, number], change: [number, number]): [number, number] {
  return [position[0] + change[0], position[1] + change[1]];
}

function sortBoxes(boxes: [number, number][], positionChange: [number, number]) {
  return boxes.toSorted(([row1, col1], [row2, col2]) => {
    if (positionChange[0] !== 0) {
      return positionChange[0] * (row2 - row1);
    }
    return positionChange[1] * (col2 - col1);
  });
}

function moveObject(current: [number, number], next: [number, number], warehouse: Matrix<string>) {
  warehouse.set(next, warehouse.get(current));
  warehouse.set(current, Type.FREE);
}

function animationConfig() {
  return {
    characterMapping: {
      '#': '░',
    },
    colorMapping: {
      '#': 26,
      '[': 137,
      ']': 137,
      '.': 232,
      '@': 48,
    },
  };
}

export async function organizeWarehouse(
  warehouse: Matrix<string>,
  moves: string[],
  determineBoxesToMove: (
    warehouse: Matrix<string>,
    robotPosition: [number, number],
    positionChange: [number, number],
  ) => [number, number][],
  config: Config,
) {
  let robotPosition = warehouse.find(Type.ROBOT)!;

  const animation = new MatrixAnimation(warehouse, config, animationConfig());
  await animation.render();

  for (const move of moves) {
    const positionChange = changes[move];
    const nextPosition = merge(robotPosition, positionChange);
    const nextValue = warehouse.get(nextPosition);

    if (nextValue === Type.FREE) {
      moveObject(robotPosition, nextPosition, warehouse);
      robotPosition = nextPosition;
    } else if (nextValue === Type.BOX_L || nextValue === Type.BOX_R || nextValue === Type.BOX) {
      const boxesToMove = sortBoxes(
        determineBoxesToMove(warehouse, robotPosition, positionChange),
        positionChange,
      );

      for (const orignalBoxPosition of boxesToMove) {
        const newBoxPosition = merge(orignalBoxPosition, positionChange);
        moveObject(orignalBoxPosition, newBoxPosition, warehouse);
      }

      if (boxesToMove.length > 0) {
        moveObject(robotPosition, nextPosition, warehouse);
        robotPosition = nextPosition;
      }
    }

    await animation.render();
  }

  animation.stop();
}
