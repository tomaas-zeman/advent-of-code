import { treeValue } from './common';

export function run(data: string[]): string | number {
  const numbers = data[0].split(' ').map((value) => parseInt(value));
  return treeValue(numbers, (numbers, childNodeSums, metadataEntries) =>
    numbers
      .splice(0, metadataEntries)
      .reduce(
        (total, index) =>
          total + (index <= 0 || index > childNodeSums.length ? 0 : childNodeSums[index - 1]),
        0,
      ),
  );
}

export const testResult = 66;
