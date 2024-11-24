import { Config } from '../..';
import { findBestGridPower } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  return findBestGridPower(parseInt(data[0]), [3]).index.join(',');
}

export const testResult = '33,45';
