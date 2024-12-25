import range from 'lodash/range';
import { Config } from '../..';
import { Matrix } from '../../aocutils';
import { CartesianProduct } from 'js-combinatorics';
import zipWith from 'lodash/zipWith';

function parse(data: string[]) {
  const locks = [];
  const keys = [];
  for (let i = 0; i < data.length; i += 8) {
    const bp = new Matrix(data.slice(i, i + 7).map((v) => v.split('')));
    const heights = range(0, bp.cols).map(
      (col) => bp.column(col).filter((v) => v === '#').length - 1,
    );
    if (bp.row(0).every((col) => col === '#')) {
      locks.push(heights);
    } else {
      keys.push(heights);
    }
  }
  return [locks, keys];
}

export async function run(data: string[], config: Config): Promise<string | number> {
  const [locks, keys] = parse(data);
  return new CartesianProduct(locks, keys)
    .toArray()
    .map((combination) => zipWith(...combination, (k, l) => k + l))
    .filter((combination) => combination.every((v) => v <= 5)).length;
}

export const testResult = 3;
