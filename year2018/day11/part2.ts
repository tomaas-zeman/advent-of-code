import { Config } from '../..';
import { findBestGridPower, initializeFuelCells } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const fuelCells = initializeFuelCells(parseInt(data[0]));

  let bestGridIndex: [number, number] = [0, 0];
  let bestGridPower = 0;
  let bestGridSize = 1;

  for (let gridSize = 1; gridSize <= 300; gridSize++) {
    const { index, power } = findBestGridPower(fuelCells, gridSize);
    if (power > bestGridPower) {
      bestGridIndex = index;
      bestGridPower = power;
      bestGridSize = gridSize;
    }
  }

  return [...bestGridIndex, bestGridSize].join(',');
}

export const testResult = '90,269,16';
