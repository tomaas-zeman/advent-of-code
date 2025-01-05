import { Config } from '../..';
import { parse, runFractalEnhancement } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const mapping = parse(data);
  return runFractalEnhancement(mapping, config.isTest ? 2 : 18).findAll('#').length;
}

export const testResult = 12;
