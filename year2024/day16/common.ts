import { DefaultMap, HashSet, Matrix, PriorityQueue } from '../../aocutils';

export type Node = [number, number];
type State = { point: Node; direction: Direction };
type Direction = 'up' | 'down' | 'left' | 'right';
type Distances = DefaultMap<Node, number>;
type Paths = DefaultMap<Node, HashSet<Node>>;

export function parse(data: string[]): [Matrix<string>, Node, Node] {
  const maze = new Matrix<string>(data.map((line) => line.split('')));
  return [maze, maze.find('S')!, maze.find('E')!];
}

export function dijkstra(maze: Matrix<string>, start: Node): [Distances, Paths] {
  const distances: Distances = new DefaultMap(Number.MAX_SAFE_INTEGER, [], true);
  for (const [row, col, value] of maze.entries().filter(([_, __, value]) => value !== '#')) {
    distances.set([row, col], value === 'S' ? 0 : Number.MAX_SAFE_INTEGER);
  }

  const paths: Paths = new DefaultMap(() => new HashSet(), [], true);
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
      const currentDistance = distances.get(next);

      if (newDistance < currentDistance) {
        distances.set(next, newDistance);
        queue.enqueue({ priority: newDistance, point: next, direction: newDirection });
        paths.set(next, new HashSet([current]));
      }

      if (newDistance === currentDistance) {
        paths.get(next).add(current);
      }

      // FIXME: this is not handling all the edge cases
      if (direction !== newDirection) {
        const changeVector = getChangeVector(direction);
        const lastNode: [number, number] = [
          next[0] + 2 * changeVector[0],
          next[1] + 2 * changeVector[1],
        ];
        if (distances.get(lastNode) + 2 === newDistance) {
          const middleNode: [number, number] = [
            next[0] + changeVector[0],
            next[1] + changeVector[1],
          ];
          paths.get(middleNode).add(lastNode);
          console.log(`${lastNode} ++ ${middleNode}`);
        }
      }
    }
  }

  return [distances, paths];
}

function getChangeVector(direction: Direction): [number, number] {
  switch (direction) {
    case 'down':
      return [-1, 0];
    case 'up':
      return [1, 0];
    case 'right':
      return [0, -1];
    case 'left':
      return [0, 1];
  }
}

function getNextDirection(direction: Direction, current: Node, next: Node) {
  if (direction === 'up') {
    if (current[1] < next[1]) {
      return 'left';
    } else if (current[1] > next[1]) {
      return 'right';
    }
  } else if (direction === 'down') {
    if (current[1] < next[1]) {
      return 'right';
    } else if (current[1] > next[1]) {
      return 'left';
    }
  } else if (direction === 'left') {
    if (current[0] < next[0]) {
      return 'up';
    } else if (current[0] > next[0]) {
      return 'down';
    }
  } else if (direction === 'right') {
    if (current[0] < next[0]) {
      return 'down';
    } else if (current[0] > next[0]) {
      return 'up';
    }
  }
  return direction;
}
