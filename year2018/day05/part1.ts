import { Config } from '../..';
import { collapsePolymer } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  return collapsePolymer(data[0], config);
}

export const testResult = 10;
