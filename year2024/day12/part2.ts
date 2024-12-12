import groupBy from 'lodash/groupBy';
import { Config } from '../..';
import { Matrix, sum } from '../../aocutils';
import { FenceConfiguration, Plot, Region, calculateFencingPrice, getFences } from './common';

function regionPrice(region: Region, garden: Matrix<Plot>): any {
  const individualFences = getFences(region, garden);
  const fencesGroupedBySide = groupBy(individualFences, ([side]) => side);
  const fencesNeeded = sum(
    Object.values(fencesGroupedBySide).map((fences) => groupFencesInLine(fences).length),
  );
  return fencesNeeded * region.length;
}

function fencesAreInLine(f1: FenceConfiguration, f2: FenceConfiguration) {
  return Math.abs(f1[1] - f2[1]) + Math.abs(f1[2] - f2[2]) === 1;
}

function groupFencesInLine(fences: FenceConfiguration[]) {
  const groups = [];

  for (const standaloneFence of fences) {
    let groupFound = false;

    // Try to find if a fence can fit to any existing group
    for (const group of groups) {
      for (const fenceInGroup of group) {
        if (fencesAreInLine(standaloneFence, fenceInGroup)) {
          groupFound = true;
          group.push(standaloneFence);
          break;
        }
      }
    }

    // If no group is found, create a new group with this fence
    if (!groupFound) {
      groups.push([standaloneFence]);
    }
  }

  return groups;
}

export async function run(data: string[], config: Config): Promise<string | number> {
  return calculateFencingPrice(data, regionPrice);
}

export const testResult = 1206;
