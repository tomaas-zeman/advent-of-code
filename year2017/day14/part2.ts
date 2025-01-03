import { Config } from '../..';
import { HashSet, Matrix, Node } from '../../aocutils';
import { createDisk } from './common';

function explore(disk: Matrix<string>, visited: HashSet<Node>, cell: Node) {
  const queue = [cell];

  while (queue.length > 0) {
    const current = queue.shift()!;
    visited.add(current);

    disk
      .neighborEntries(current, false)
      .filter(([row, col, value]) => !visited.has([row, col]) && value === '1')
      .forEach(([row, col, _]) => queue.push([row, col]));
  }
}

export async function run(data: string[], config: Config): Promise<string | number> {
  const disk = await createDisk(data, config);
  const visited = new HashSet<Node>();
  let groups = 0;

  for (const [row, col, value] of disk.entries()) {
    if (visited.has([row, col]) || value === '0') {
      continue;
    }
    explore(disk, visited, [row, col]);
    groups++;
  }

  return groups;
}

export const testResult = 1242;
