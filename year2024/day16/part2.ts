import { Config } from '../..';
import { HashSet, MatrixAnimation } from '../../aocutils';
import { dijkstra, parse, Node } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const [maze, start, end] = parse(data);
  const [_, paths] = dijkstra(maze, start);

  const visited = new HashSet<Node>();

  const queue: Node[] = [...paths.get(end).values()];
  while (queue.length > 0) {
    const current = queue.pop()!;
    visited.add(current);
    queue.push(...[...paths.get(current).values()]);
  }

  // const printable = maze.clone();
  // for (const [row, col] of visited.values()) {
  //   printable.set(row, col, 'O');
  // }
  // printable.set(printable.find('E')!, 'O');
  // const animation = new MatrixAnimation(printable);
  // await animation.render();

  return visited.size;
}

export const testResult = 64;
