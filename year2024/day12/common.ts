import { Matrix, sum } from '../../aocutils';

export type Plot = { name: string; visited: boolean };
export type Region = [number, number][];
export type FenceConfiguration = [FenceSide, number, number];

enum FenceSide {
  LEFT,
  RIGHT,
  UP,
  DOWN,
}

const fenceOptions: FenceConfiguration[] = [
  [FenceSide.LEFT, 0, -1],
  [FenceSide.RIGHT, 0, 1],
  [FenceSide.UP, -1, 0],
  [FenceSide.DOWN, 1, 0],
];

function parse(data: string[]) {
  return new Matrix<Plot>(
    data.map((line) => line.split('').map((name) => ({ name, visited: false }))),
  ).pad(1, { name: '0', visited: true });
}

function exploreRegion(startRow: number, startCol: number, garden: Matrix<Plot>) {
  const region: Region = [];

  const queue: Region = [[startRow, startCol]];
  while (queue.length > 0) {
    const [row, col] = queue.shift()!;

    const plot = garden.get(row, col);
    if (plot.visited) {
      continue;
    }
    plot.visited = true;
    region.push([row, col]);

    queue.push(
      ...garden.neighborPositions(row, col, false).filter(([row, col]) => {
        const { visited, name } = garden.get(row, col);
        return !visited && name === plot.name;
      }),
    );
  }

  return region;
}

export function calculateFencingPrice(
  data: string[],
  regionPrice: (region: Region, garden: Matrix<Plot>) => number,
) {
  const garden = parse(data);
  const regions: Region[] = [];

  for (const [row, col, { visited }] of garden.entries()) {
    if (!visited) {
      regions.push(exploreRegion(row, col, garden));
    }
  }

  return sum(regions.map((region) => regionPrice(region, garden)));
}

export function getFences(region: Region, garden: Matrix<Plot>) {
  const name = garden.get(...region[0]).name;

  const fences: FenceConfiguration[] = [];

  for (const [row, col] of region) {
    for (const [side, rowChange, colChange] of fenceOptions) {
      const plot = garden.get(row + rowChange, col + colChange);
      if (plot.name !== name) {
        fences.push([side, row, col]);
      }
    }
  }

  return fences;
}
