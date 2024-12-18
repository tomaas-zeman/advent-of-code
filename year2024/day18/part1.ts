import { Config } from '../..';
import { dijkstra, Matrix } from '../../aocutils';
import { parse } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const [bytes, [width, height]] = parse(data, config);

  const memory = Matrix.create(width, height, '.');
  for (const [col, row] of bytes.slice(0, config.isTest ? 12 : 1024)) {
    memory.set(row, col, '#');
  }

  const distances = dijkstra(memory, [0, 0], ['.']);
  return distances.get([width - 1, height - 1]);
}

export const testResult = 22;
