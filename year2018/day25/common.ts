export type Point = [number, number, number, number];

export function manhattan(p1: Point, p2: Point) {
  return p1.reduce((sum, _, i) => sum + Math.abs(p1[i] - p2[i]), 0);
}

export function parse(data: string[]): Point[] {
  return data.map((line) => line.split(',').map((value) => parseInt(value)) as Point);
}
