// https://www.redblobgames.com/grids/hexagons
// doubled coordinates (double-height)
export type Direction = 'sw' | 'nw' | 'n' | 's' | 'ne' | 'se';
export type Point = [number, number, number];

const positionChange: Record<Direction, Point> = {
  nw: [0, -1, 1],
  sw: [-1, 0, 1],
  n: [1, -1, 0],
  s: [-1, 1, 0],
  ne: [1, 0, -1],
  se: [0, 1, -1],
};

export function distance(p1: Point, p2: Point) {
  return Math.max(Math.abs(p1[0] - p2[0]), Math.abs(p1[1] - p2[1]), Math.abs(p1[2] - p2[2]));
}

export function nextPosition(position: Point, move: Direction) {
  return position.map((coord, i) => coord + positionChange[move][i]) as Point;
}

export function parse(data: string[]) {
  return data[0].split(',') as Direction[];
}
