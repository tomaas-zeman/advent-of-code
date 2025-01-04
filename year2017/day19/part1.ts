import { Config } from '../..';
import { parse, walkPath } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const pipes = parse(data);
  const [message] = walkPath(pipes);
  return message;
}

export const testResult = 'ABCDEF';
