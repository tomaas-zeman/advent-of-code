import { Config } from '../..';
import { Matrix, sum } from '../../aocutils';

type Coord = { row: number; col: number };

type Item = {
  erosionLevel: number;
  geologicIndex: number;
  type: Type;
};

enum Type {
  ROCKY = 0,
  WET = 1,
  NARROW = 2,
}
const types = [Type.ROCKY, Type.WET, Type.NARROW];

function parse(data: string[]): [number, Coord] {
  const depth = parseInt(data[0].split(' ')[1]);
  const [row, col] = data[1]
    .split(' ')[1]
    .split(',')
    .map((v) => parseInt(v));
  return [depth, { row, col }];
}

function evaluateCaveRegion(row: number, col: number, depth: number, cave: Matrix<Item>) {
  let geologicIndex = 0;
  if ((row === 0 && col === 0) || (row === cave.rows - 1 && col === cave.cols - 1)) {
    geologicIndex = 0;
  } else if (col === 0) {
    geologicIndex = row * 16807;
  } else if (row === 0) {
    geologicIndex = col * 48271;
  } else {
    geologicIndex = cave.get(row, col - 1).erosionLevel * cave.get(row - 1, col).erosionLevel;
  }

  const erosionLevel = (geologicIndex + depth) % 20183;
  const type = types[erosionLevel % 3];
  cave.set(row, col, { erosionLevel, geologicIndex, type });
}

export async function run(data: string[], config: Config): Promise<string | number> {
  const [depth, target] = parse(data);
  const cave = Matrix.create(target.row + 1, target.col + 1, {
    erosionLevel: 0,
    geologicIndex: 0,
    type: Type.ROCKY,
  });

  for (const [row, col] of cave.positions()) {
    evaluateCaveRegion(row, col, depth, cave);
  }

  return sum(
    cave.slice(0, target.row + 1, 0, target.col + 1).flatMap((row) => row.map((col) => col.type)),
  );
}

export const testResult = 114;
