import { Matrix } from '../../aocutils';

export function findBestGridPower(sn: number, gridSizes: number[]) {
  const prefixSum = initializeFuelCells(sn);
  for (let row = 1; row < prefixSum.rows; row++) {
    for (let col = 1; col < prefixSum.cols; col++) {
      prefixSum.set(row, col, prefixSum.get(row, col) + prefixSum.get(row, col - 1));
    }
  }
  for (let col = 1; col < prefixSum.rows; col++) {
    for (let row = 1; row < prefixSum.cols; row++) {
      prefixSum.set(row, col, prefixSum.get(row, col) + prefixSum.get(row - 1, col));
    }
  }

  let bestGridIndex: [number, number] = [0, 0];
  let bestGridPower = 0;
  let bestGridSize = 1;

  for (let gridSize of gridSizes) {
    const { index, power } = bestPowerForGridSize(prefixSum, gridSize);
    if (power > bestGridPower) {
      bestGridIndex = index;
      bestGridPower = power;
      bestGridSize = gridSize;
    }
  }

  return { power: bestGridPower, index: bestGridIndex, gridSize: bestGridSize };
}

function initializeFuelCells(sn: number): Matrix<number> {
  function cellPowerLevel(x: number, y: number) {
    const rackId = x + 10;
    const basePowerLevel = (rackId * y + sn) * rackId;
    return parseInt(basePowerLevel.toString().slice(-3, -2) || '0') - 5;
  }

  // Pad with zeros to prepare for prefix sum - hence the size 301
  const fuelCells = Matrix.create(301, 301, 0);

  for (let row = 1; row < fuelCells.rows; row++) {
    for (let col = 1; col < fuelCells.cols; col++) {
      fuelCells.set(row, col, cellPowerLevel(row, col));
    }
  }

  return fuelCells;
}

function bestPowerForGridSize(
  prefixSum: Matrix<number>,
  gridSize: number,
): { power: number; index: [number, number] } {
  let bestGridIndex: [number, number] = [0, 0];
  let bestGridPower = 0;

  for (let row = gridSize; row < prefixSum.rows; row++) {
    for (let col = gridSize; col < prefixSum.cols; col++) {
      const power =
        prefixSum.get(row, col) -
        prefixSum.get(row - gridSize, col) -
        prefixSum.get(row, col - gridSize) +
        prefixSum.get(row - gridSize, col - gridSize);
      if (power > bestGridPower) {
        bestGridIndex = [row - gridSize + 1, col - gridSize + 1];
        bestGridPower = power;
      }
    }
  }

  return { power: bestGridPower, index: bestGridIndex };
}
