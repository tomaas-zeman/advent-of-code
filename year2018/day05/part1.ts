import { collapsePolymer } from './common';

export function run(data: string[], isTest?: boolean): string | number {
  return collapsePolymer(data[0], isTest);
}

export const testResult = 10;
