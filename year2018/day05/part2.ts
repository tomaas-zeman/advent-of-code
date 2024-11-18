import { Config } from '../..';
import { collapsePolymer } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const letters = [...new Set(data[0].toLowerCase().split('')).values()];
  const result: number[] = [];
  for (let i = 0; i < letters.length; i++) {
    const value = await collapsePolymer(
      data[0].replaceAll(letters[i], '').replaceAll(letters[i].toUpperCase(), ''),
      config,
    );
    result.push(value);
  }
  return Math.min(...result);
}

export const testResult = 4;
