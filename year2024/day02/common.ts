import { nwise } from '../../aocutils';

export function parseReports(data: string[]) {
  return data.map((line) => line.split(' ').asInt());
}

export function isSafe(report: number[]) {
  const diffs = nwise(report).map(([prev, next]) => next - prev);
  return diffs.every((v) => v >= 1 && v <= 3) || diffs.every((v) => v <= -1 && v >= -3);
}
