import { flatten, index, matrix, Matrix, range, subset, zeros } from 'mathjs';

export function findBestGridPower(
  fuelCells: Matrix,
  gridSize: number,
): { power: number; index: [number, number] } {
  const prefixSum = fuelCells.clone();
  for (let row = 1; row < fuelCells.size()[0]; row++) {
    for (let col = 1; col < fuelCells.size()[1]; col++) {
      prefixSum.set([row, col], prefixSum.get([row, col]) + prefixSum.get([row, col - 1]));
    }
  }

  for (let col = 1; col < fuelCells.size()[1]; col++) {
    for (let row = 1; row < fuelCells.size()[0]; row++) {
      prefixSum.set([row, col], prefixSum.get([row, col]) + prefixSum.get([row - 1, col]));
    }
  }

  let bestGridIndex: [number, number] = [0, 0];
  let bestGridPower = 0;

  for (let row = gridSize; row < fuelCells.size()[0]; row++) {
    for (let col = gridSize; col < fuelCells.size()[1]; col++) {
      const power =
        prefixSum.get([row, col]) -
        prefixSum.get([row - gridSize, col]) -
        prefixSum.get([row, col - gridSize]) +
        prefixSum.get([row - gridSize, col - gridSize]);
      if (power > bestGridPower) {
        bestGridIndex = [row - gridSize + 1, col - gridSize + 1];
        bestGridPower = power;
      }
    }
  }

  return { power: bestGridPower, index: bestGridIndex };
}

export function initializeFuelCells(sn: number) {
  const fuelCells = matrix(zeros(301, 301));
  for (let row = 1; row < fuelCells.size()[0]; row++) {
    for (let col = 1; col < fuelCells.size()[1]; col++) {
      fuelCells.set([row, col], cellPowerLevel(row, col, sn));
    }
  }
  return fuelCells;
}

function cellPowerLevel(x: number, y: number, sn: number) {
  const rackId = x + 10;
  const basePowerLevel = (rackId * y + sn) * rackId;
  return parseInt(basePowerLevel.toString().slice(-3, -2) || '0') - 5;
}
