import { Config } from '../..';
import { countAntinodes, parse } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const [antennas, areaSize] = parse(data);
  return countAntinodes(antennas, areaSize, [1]);
}

export const testResult = 14;
