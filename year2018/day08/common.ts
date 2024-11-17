import { sum } from 'mathjs';

export function treeValue(
  numbers: number[],
  computeMainNodeValue: (
    numbers: number[],
    childNodeSums: number[],
    metadataEntries: number,
  ) => number,
): number {
  if (!numbers.length) {
    return 0;
  }

  const childNodes = numbers.shift()!;
  const metadataEntries = numbers.shift()!;

  if (childNodes === 0) {
    return sum(numbers.splice(0, metadataEntries));
  }

  const childNodeSums = new Array(childNodes).fill(0);
  for (let i = 0; i < childNodes; i++) {
    childNodeSums[i] = treeValue(numbers, computeMainNodeValue);
  }

  return computeMainNodeValue(numbers, childNodeSums, metadataEntries);
}
