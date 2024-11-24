import { flatten, index, matrix, Matrix, range, subset, zeros } from 'mathjs';

export function findBestGridPower(
  fuelCells: Matrix,
  gridSize: number,
): { power: number; index: [number, number] } {
  let bestGridIndex: [number, number] = [0, 0];
  let bestGridPower = 0;

  for (let row = 0; row < fuelCells.size()[0] - (gridSize - 1); row++) {
    for (let col = 0; col < fuelCells.size()[1] - (gridSize - 1); col++) {
      const power = gridPowerLevel(fuelCells, row, col, gridSize);
      if (power > bestGridPower) {
        bestGridIndex = [row, col];
        bestGridPower = power;
      }
    }
  }

  return { power: bestGridPower, index: bestGridIndex };
}

export function initializeFuelCells(sn: number) {
  const fuelCells = matrix(zeros(300, 300));
  for (let row = 0; row < fuelCells.size()[0]; row++) {
    for (let col = 0; col < fuelCells.size()[1]; col++) {
      fuelCells.set([row, col], cellPowerLevel(row + 1, col + 1, sn));
    }
  }
  return fuelCells;
}

function cellPowerLevel(x: number, y: number, sn: number) {
  const rackId = x + 10;
  const basePowerLevel = (rackId * y + sn) * rackId;
  return parseInt(basePowerLevel.toString().slice(-3, -2) || '0') - 5;
}

function gridPowerLevel(fuelCells: Matrix, x: number, y: number, gridSize: number): number {
  const grid = subset(fuelCells, index(range(x, x + gridSize), range(y, y + gridSize)));
  if (typeof grid === 'number') {
    return grid;
  }
  return (flatten(grid).toArray() as number[]).reduce((sum, value) => sum + value, 0);
}
