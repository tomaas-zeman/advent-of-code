import { parse } from './common';

export function run(data: string[]): string | number {
  const [pointOverlaps, _] = parse(data);
  return Object.values(pointOverlaps).filter((overlaps) => overlaps > 1).length;
}

export const testResult = 4;
