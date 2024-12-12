import { Config } from '../..';
import { Matrix } from '../../aocutils';
import { Plot, Region, calculateFencingPrice, getFences } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  return calculateFencingPrice(
    data,
    (region, garden) => getFences(region, garden).length * region.length,
  );
}

export const testResult = 1930;
