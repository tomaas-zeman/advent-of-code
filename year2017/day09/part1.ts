import { Config } from '../..';
import { processStream } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const [score] = processStream(data);
  return score;
}

export const testResult = 3;
