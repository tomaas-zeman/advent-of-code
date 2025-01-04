// https://www.redblobgames.com/grids/hexagons

import { Point3D } from "../../aocutils";

// doubled coordinates (double-height)
export type Direction = 'sw' | 'nw' | 'n' | 's' | 'ne' | 'se';

const positionChange: Record<Direction, Point3D> = {
  nw: [0, -1, 1],
  sw: [-1, 0, 1],
  n: [1, -1, 0],
  s: [-1, 1, 0],
  ne: [1, 0, -1],
  se: [0, 1, -1],
};

export function distance(p1: Point3D, p2: Point3D) {
  return Math.max(Math.abs(p1[0] - p2[0]), Math.abs(p1[1] - p2[1]), Math.abs(p1[2] - p2[2]));
}

export function nextPosition(position: Point3D, move: Direction) {
  return position.map((coord, i) => coord + positionChange[move][i]) as Point3D;
}

export function parse(data: string[]) {
  return data[0].split(',') as Direction[];
}
