import { Config } from '../..';
import { parse } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const [pointOverlaps, _] = parse(data);
  return Object.values(pointOverlaps).filter((overlaps) => overlaps > 1).length;
}

export const testResult = 4;
