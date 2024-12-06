import { Config } from '../..';
import { treeValue } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const numbers = data[0].split(' ').asInt();
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
