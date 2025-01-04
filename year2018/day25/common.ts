export type Point = [number, number, number, number];

export function parse(data: string[]): Point[] {
  return data.map((line) => line.split(',').asInt() as Point);
}
