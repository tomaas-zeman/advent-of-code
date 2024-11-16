import { collapsePolymer } from './common';

export function run(data: string[]): string | number {
  const letters = new Set(data[0].toLowerCase().split(''));
  return Math.min(
    ...[...letters.values()].map((letter) =>
      collapsePolymer(data[0].replaceAll(letter, '').replaceAll(letter.toUpperCase(), '')),
    ),
  );
}

export const testResult = 4;
