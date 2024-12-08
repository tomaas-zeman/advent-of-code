import range from 'lodash/range';
import { Config } from '../..';
import { countAntinodes, parse } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const [antennas, areaSize] = parse(data);
  return countAntinodes(antennas, areaSize, range(0, Math.max(...areaSize)));
}

export const testResult = 34;
