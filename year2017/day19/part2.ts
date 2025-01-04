import { Config } from '../..';
import { parse, walkPath } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const pipes = parse(data);
  const [_, steps] = walkPath(pipes);
  return steps;
}

export const testResult = 38;
