import { treeValue } from './common';
import { Config } from '../..';
import { sum } from '../../aocutils';

export async function run(data: string[], config: Config): Promise<string | number> {
  const numbers = data[0].split(' ').asInt();
  return treeValue(
    numbers,
    (numbers, childNodeSums, metadataEntries) =>
      sum(childNodeSums) + sum(numbers.splice(0, metadataEntries)),
  );
}

export const testResult = 138;
