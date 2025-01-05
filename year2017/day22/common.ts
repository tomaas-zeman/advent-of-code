import { DefaultMap, mergePoints, mod, Node } from '../../aocutils';

export enum State {
  INFECTED = '#',
  CLEAN = '.',
  WEAKENED = 'W',
  FLAGGED = 'F',
}

type Cluster = DefaultMap<Node, State>;
type Direction = 'down' | 'up' | 'left' | 'right';

const directions: Direction[] = ['up', 'right', 'down', 'left'];

const changes: Record<Direction, Node> = {
  down: [1, 0],
  up: [-1, 0],
  left: [0, -1],
  right: [0, 1],
};

function nextDirection(cluster: Cluster, direction: Direction, position: Node) {
  const directionChange = {
    [State.CLEAN]: -1,
    [State.WEAKENED]: 0,
    [State.INFECTED]: 1,
    [State.FLAGGED]: 2,
  }[cluster.get(position)];
  return directions[mod(directions.indexOf(direction) + directionChange!, directions.length)];
}

function parse(data: string[]) {
  const cluster: Cluster = new DefaultMap(State.CLEAN, true);

  for (let row = 0; row < data.length; row++) {
    for (let col = 0; col < data[0].length; col++) {
      cluster.set([row, col], data[row][col] as State);
    }
  }

  return cluster;
}

export function countInfections(data: string[], states: State[], cycles: number) {
  const cluster = parse(data);

  let position: Node = [Math.floor(data.length / 2), Math.floor(data[0].length / 2)];
  let direction: Direction = 'up';
  let infections = 0;

  for (let cycle = 0; cycle < cycles; cycle++) {
    direction = nextDirection(cluster, direction, position);

    cluster.mapItem(position, (s) => states[mod(states.indexOf(s) + 1, states.length)]);
    if (cluster.get(position) === State.INFECTED) {
      infections++;
    }

    position = mergePoints(position, changes[direction]);
  }

  return infections;
}
