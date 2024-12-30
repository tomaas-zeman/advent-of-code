import { Config } from '../..';
import { Matrix, sum } from '../../aocutils';

type Range = {
  range: {
    start: number;
    end: number;
    step: number;
  };
  cell: (i: number) => [number, number];
};

function fillNumbers(spiral: Matrix<number>, stopValue: number): number | undefined {
  const ranges: Range[] = [
    { range: { start: spiral.rows - 2, end: 0, step: -1 }, cell: (i) => [i, spiral.cols - 1] },
    { range: { start: spiral.cols - 1, end: -1, step: -1 }, cell: (i) => [0, i] },
    { range: { start: 1, end: spiral.rows - 1, step: 1 }, cell: (i) => [i, 0] },
    { range: { start: 0, end: spiral.cols, step: 1 }, cell: (i) => [spiral.rows - 1, i] },
  ];

  for (const { range, cell } of ranges) {
    const { start, end, step } = range;
    for (let i = start; i !== end; i += step) {
      const currentCell = cell(i);
      const value = sum(spiral.neighbors(currentCell, true));
      if (value >= stopValue) {
        return value;
      }
      spiral.set(currentCell, value);
    }
  }
}

export async function run(data: string[], config: Config): Promise<string | number> {
  const stopValue = parseInt(data[0]);
  let spiral = new Matrix<number>([[1]]);

  while (true) {
    spiral = spiral.pad(1, 0);
    const result = fillNumbers(spiral, stopValue);
    if (result) {
      return result;
    }
  }
}

export const testResult = 1968;
