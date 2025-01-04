import { Matrix, Node } from '../../aocutils';

enum Type {
  PIPE_V = '|',
  PIPE_H = '-',
  PIPE_X = '+',
  NOTHING = ' ',
}

type Direction = 'down' | 'up' | 'left' | 'right';

const positionChanges: Record<Direction, Node> = {
  down: [1, 0],
  up: [-1, 0],
  left: [0, -1],
  right: [0, 1],
};

function merge(n1: Node, n2: Node): Node {
  return [n1[0] + n2[0], n1[1] + n2[1]];
}

export function walkPath(pipes: Matrix<string>): [string, number] {
  let position: Node = [0, pipes.row(0).indexOf(Type.PIPE_V)];
  let direction: Direction = 'down';
  let steps = 0;
  const message = [];

  while (true) {
    const value = pipes.get(position);

    if (value.match(/[A-Z]/)) {
      message.push(value);
    }
    if (value === Type.NOTHING) {
      break;
    }

    if (value === Type.PIPE_X) {
      const nextDirections: Direction[] = ['up', 'down'].includes(direction)
        ? ['left', 'right']
        : ['up', 'down'];
      for (const nextDirection of nextDirections) {
        const nextPosition = merge(position, positionChanges[nextDirection]);
        if (pipes.get(nextPosition) !== Type.NOTHING) {
          position = nextPosition;
          direction = nextDirection;
          break;
        }
      }
    } else {
      position = merge(position, positionChanges[direction]);
    }

    steps++;
  }

  return [message.join(''), steps];
}

export function parse(data: string[]) {
  return new Matrix<string>(data.map((line) => line.split('')));
}
