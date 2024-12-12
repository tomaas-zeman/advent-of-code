import { Matrix } from '../../aocutils';

export enum Tile {
  OBSTACLE = '#',
  GUARD = '^',
  VISITED = 'X',
}

export const MOVEMENT_CHANGES: [number, number][] = [
  [-1, 0],
  [0, 1],
  [1, 0],
  [0, -1],
];

export function parse(data: string[]): [Matrix<string>, [number, number]] {
  const startingMap = new Matrix(data.map((line) => line.split('')));
  const startingPosition = startingMap.find(Tile.GUARD)!;
  return [startingMap, startingPosition];
}
