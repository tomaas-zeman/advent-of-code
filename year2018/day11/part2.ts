import { Config } from '../..';
import { findBestGridPower } from './common';
import { range } from 'mathjs';

export async function run(data: string[], config: Config): Promise<string | number> {
  const { index, gridSize } = findBestGridPower(
    parseInt(data[0]),
    range(1, 300).toArray() as number[],
  );
  return [...index, gridSize].join(',');
}

export const testResult = '90,269,16';
