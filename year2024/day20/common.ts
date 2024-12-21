import { DefaultMap, isEqual, Matrix, Node } from '../../aocutils';

export function parse(data: string[]) {
  const map = new Matrix<string>(data.map((line) => line.split('')));
  const start = map.find('S')!;
  const end = map.find('E')!;
  map.set(start, '.');
  map.set(end, '.');

  return getDistances(map, start, end);
}

function getDistances(map: Matrix<string>, start: Node, end: Node) {
  const distances = new DefaultMap<Node, number>(0, [], true);

  let current = start;
  while (true) {
    distances.set(current, distances.size);

    if (isEqual(current, end)) {
      break;
    }

    current = map
      .neighborPositions(current, false)
      .filter((node) => map.get(node) === '.' && !distances.has(node))[0];
  }

  return distances;
}

export function sumCheats(cheats: DefaultMap<number, number>, threshold: number) {
  let sum = 0;
  for (const [timeSaving, count] of cheats.entries()) {
    if (timeSaving >= threshold) {
      sum += count;
    }
  }
  return sum;
}

export function findFastCheats(distances: DefaultMap<Node, number>, range: number) {
  const pathLength = distances.size - 1;
  const nodes = [...distances.keys()];
  const cheats = new DefaultMap<number, number>(0);

  for (const start of nodes) {
    for (const [end, cheatPartLength] of cheatPathsInRange(nodes, start, range)) {
      const cheatPath = distances.get(start) + (pathLength - distances.get(end)) + cheatPartLength;
      if (cheatPath < pathLength) {
        cheats.mapItem(pathLength - cheatPath, (v) => v + 1);
      }
    }
  }

  return cheats;
}

function cheatPathsInRange(nodes: Node[], start: Node, range: number): [Node, number][] {
  const cheatPaths: [Node, number][] = [];

  for (const node of nodes) {
    if (isEqual(node, start)) {
      continue;
    }
    if (manhattan(node, start) <= range) {
      cheatPaths.push([node, manhattan(node, start)]);
    }
  }

  return cheatPaths;
}

function manhattan(a: Node, b: Node) {
  return Math.abs(a[0] - b[0]) + Math.abs(a[1] - b[1]);
}
