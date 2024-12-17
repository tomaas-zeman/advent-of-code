import { Config } from '../..';
import { dijkstra, parse } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const [maze, start, end] = parse(data);
  const distances = dijkstra(maze, start);
  return distances.get(end);
}

export const testResult = 7036;
