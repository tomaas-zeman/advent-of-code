import { Config } from '../..';
import { dance, init } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  return dance(...init(data, config), 1);
}

export const testResult = 'baedc';
