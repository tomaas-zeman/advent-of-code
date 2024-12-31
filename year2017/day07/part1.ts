import { Config } from '../..';
import { findRoot, parse } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const programs = parse(data);
  return findRoot(programs);
}

export const testResult = 'tknk';
