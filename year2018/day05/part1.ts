import { collapsePolymer } from './common';

export function run(data: string[]): string | number {
  return collapsePolymer(data[0]);
}

export const testResult = 10;
