import { Config } from '../..';
import { processStream } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const [_, garbage] = processStream(data);
  return garbage;
}

export const testResult = 10;
