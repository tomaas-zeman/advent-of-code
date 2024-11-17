import { sum } from 'mathjs';
import { treeValue } from './common';

export function run(data: string[]): string | number {
  const numbers = data[0].split(' ').map((value) => parseInt(value));
  return treeValue(
    numbers,
    (numbers, childNodeSums, metadataEntries) =>
      sum(childNodeSums) + sum(numbers.splice(0, metadataEntries)),
  );
}

export const testResult = 138;
