import { Config } from '../..';

export async function run(data: string[], config: Config): Promise<string | number> {
  return data
    .map((line) => line.split(' '))
    .filter((words) => new Set(words).size === words.length)
    .length;
}

export const testResult = 2;
