import { DefaultMap, HashSet, Matrix, PriorityQueue } from '../../aocutils';

export type Node = [number, number];
type State = { point: Node; direction: Direction };
type Direction = 'up' | 'down' | 'left' | 'right';
type Distances = DefaultMap<Node, number>;

export function parse(data: string[]): [Matrix<string>, Node, Node] {
  const maze = new Matrix<string>(data.map((line) => line.split('')));
  return [maze, maze.find('S')!, maze.find('E')!];
}

export function dijkstra(maze: Matrix<string>, start: Node): Distances {
  const distances: Distances = new DefaultMap(Number.MAX_SAFE_INTEGER, [], true);
  for (const [row, col, value] of maze.entries().filter(([_, __, value]) => value !== '#')) {
    distances.set([row, col], value === maze.get(start) ? 0 : Number.MAX_SAFE_INTEGER);
  }

  const visited = new HashSet<Node>();

  const queue = new PriorityQueue<State>([{ priority: 0, point: start, direction: 'right' }]);
  while (queue.size() > 0) {
    const { point: current, direction } = queue.dequeue()!;

    visited.add(current);

    const neighbors = maze
      .neighborPositions(current, false)
      .filter((node) => !visited.has(node) && maze.get(node) !== '#');

    for (const next of neighbors) {
      const newDirection = getNextDirection(direction, current, next);
      const edgeLength = direction === newDirection ? 1 : 1001;
      const newDistance = distances.get(current) + edgeLength;

      if (newDistance <= distances.get(next)) {
        distances.set(next, newDistance);
        queue.enqueue({ priority: newDistance, point: next, direction: newDirection });
      }
    }
  }

  return distances;
}

function getNextDirection(direction: Direction, current: Node, next: Node): Direction {
  const dx = next[0] - current[0];
  const dy = next[1] - current[1];
  const turns: Record<Direction, Record<string, Direction>> = {
    up: { positive: 'left', negative: 'right' },
    down: { positive: 'right', negative: 'left' },
    left: { positive: 'up', negative: 'down' },
    right: { positive: 'down', negative: 'up' },
  };

  const diff = ['left', 'right'].includes(direction) ? dx : dy;
  if (diff > 0) {
    return turns[direction].positive;
  }
  if (diff < 0) {
    return turns[direction].negative;
  }
  return direction;
}
