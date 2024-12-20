import { Config } from '../..';
import { findFastCheats, parse, sumCheats } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const distances = parse(data);
  const cheats = findFastCheats(distances, 20);
  return sumCheats(cheats, config.isTest ? 50 : 100);
}

export const testResult = 285;
