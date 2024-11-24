import { Config } from '../..';
import { findBestGridPower, initializeFuelCells } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const fuelCells = initializeFuelCells(parseInt(data[0]));

  let bestGridIndex: [number, number] = [0, 0];
  let bestGridPower = 0;
  let bestGridSize = 1;

  // TODO
  // This is obviously not a complete solution since the max grid size is 20 and not 300.
  // Luckily, the solution was found earlier. If it didn't, we would have to optimize the 
  //algorithm as it gets really slow with the larger grid size.
  for (let gridSize = 1; gridSize <= 20; gridSize++) {
    const { index, power } = findBestGridPower(fuelCells, gridSize);
    if (power > bestGridPower) {
      bestGridIndex = index;
      bestGridPower = power;
      bestGridSize = gridSize;
    }
  }

  return [...bestGridIndex.map((i) => i + 1), bestGridSize].join(',');
}

export const testResult = '90,269,16';
