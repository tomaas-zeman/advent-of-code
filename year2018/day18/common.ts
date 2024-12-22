import countBy from 'lodash/countBy';
import { Matrix } from '../../aocutils';

enum Type {
  OPEN = '.',
  LUMBERYARD = '#',
  TREE = '|',
}

function parseMatrix(data: string[]): Matrix<string> {
  return new Matrix<string>(data.map((line) => line.split('')));
}

export function calculateResourceValue(data: string[], minutes: number): number {
  const states: Record<string, number> = {};
  let forest = parseMatrix(data);

  for (let time = 0; time < minutes; time++) {
    if (forest.data.flatMap((row) => row).every((acre) => acre === Type.OPEN)) {
      break;
    }

    const newForest = forest.clone();

    for (let row = 0; row < forest.rows; row++) {
      for (let col = 0; col < forest.cols; col++) {
        const neighbors = countBy(forest.neighbors(row, col));

        switch (forest.get(row, col)) {
          case Type.OPEN:
            if (neighbors[Type.TREE] >= 3) {
              newForest.set(row, col, Type.TREE);
            }
            break;
          case Type.LUMBERYARD:
            if (!(neighbors[Type.LUMBERYARD] >= 0 && neighbors[Type.TREE] >= 0)) {
              newForest.set(row, col, Type.OPEN);
            }
            break;
          case Type.TREE:
            if (neighbors[Type.LUMBERYARD] >= 3) {
              newForest.set(row, col, Type.LUMBERYARD);
            }
            break;
        }
      }
    }

    forest = newForest;

    const hash = forest.hash();
    const lastTime = states[hash];
    if (lastTime) {
      const repeats = Math.floor((minutes - lastTime) / (time - lastTime));
      time += (repeats - 1) * (time - lastTime);
    }
    states[hash] = time;
  }

  const acres = countBy(forest.data.flatMap((row) => row));
  return acres[Type.LUMBERYARD] * acres[Type.TREE] || 0;
}
