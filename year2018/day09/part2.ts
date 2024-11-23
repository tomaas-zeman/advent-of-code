import { Config } from '../..';
import { computeScores, parseData } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const [players, marbles] = parseData(data);
  return computeScores(players, marbles * 100);
}

export const testResult = 74765078;
