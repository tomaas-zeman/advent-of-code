import { Config } from '../..';
import { sum } from '../../aocutils';
import { exploreCave, parse } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const [depth, target] = parse(data);
  const cave = exploreCave(depth, target);
  return sum(
    cave.slice(0, target.row + 1, 0, target.col + 1).flatMap((row) => row.map((col) => col.type)),
  );
}

export const testResult = 114;
