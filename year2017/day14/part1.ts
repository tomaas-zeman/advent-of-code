import { Config } from '../..';
import { createDisk } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  return (await createDisk(data, config)).findAll('1').length;
}

export const testResult = 8108;
