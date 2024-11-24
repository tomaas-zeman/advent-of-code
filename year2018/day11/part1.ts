import { Config } from '../..';
import { findBestGridPower, initializeFuelCells } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const fuelCells = initializeFuelCells(parseInt(data[0]));
  return findBestGridPower(fuelCells, 3)
    .index.map((i) => i + 1)
    .join(',');
}

export const testResult = '33,45';
