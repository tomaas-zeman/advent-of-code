import { Matrix, mod } from '../../aocutils';

const TURN_ORDER = ['<', '^', '>', 'v'];
const POSITION_CHANGE = {
  '<': [0, -1],
  '>': [0, 1],
  '^': [-1, 0],
  v: [1, 0],
};


export class Cart {
  direction: string;
  position: [number, number];

  private turnIndex = 0;

  constructor(direction: string, position: [number, number]) {
    this.direction = direction;
    this.position = position;
  }

  turn(tile: string) {
    if (tile === '+') {
      const turnChanges = [-1, 0, 1];
      this.direction =
        TURN_ORDER[
          mod(
            TURN_ORDER.indexOf(this.direction) + turnChanges[this.turnIndex % turnChanges.length],
            TURN_ORDER.length,
          )
        ];
      this.turnIndex++;
      return;
    }

    const changes = {
      '>': { '\\': 'v', '/': '^' },
      '<': { '\\': '^', '/': 'v' },
      '^': { '\\': '<', '/': '>' },
      v: { '\\': '>', '/': '<' },
    };
    this.direction = changes[this.direction][tile];
  }

  move(tracks: Matrix<string>) {
    // Move
    const position: [number, number] = [
      this.position[0] + POSITION_CHANGE[this.direction][0],
      this.position[1] + POSITION_CHANGE[this.direction][1],
    ];
    this.position = position;

    // Turn if bend or intersection
    const tile = tracks.get(this.position);
    if ('+\\/'.includes(tile)) {
      this.turn(tile);
    }

    return position;
  }

  positionAsString(): string {
    return `${this.position[1]},${this.position[0]}`;
  }
}

function extractCarts(tracks: Matrix<string>) {
  const carts: Cart[] = [];
  for (let [row, col, direction] of tracks.entries()) {
    if (TURN_ORDER.includes(direction)) {
      carts.push(new Cart(direction, [row, col]));
      tracks.set(row, col, '<>'.includes(direction) ? '-' : '|');
    }
  }
  return carts;
}

export function parseInput(data: string[]): [Matrix<string>, Cart[]] {
  const tracks = new Matrix<string>(data.map((line) => line.split('')));
  const carts = extractCarts(tracks);
  return [tracks, carts];
}

export function initTick(carts: Cart[]): [Cart[], Set<string>] {
  const orderedCarts = carts.sort((c1, c2) => {
    const rowDiff = c1.position[0] - c2.position[0];
    if (rowDiff !== 0) {
      return rowDiff;
    }
    return c1.position[1] - c2.position[1];
  });
  const cartPositions = new Set(carts.map((cart) => cart.positionAsString()));
  return [orderedCarts, cartPositions];
}
