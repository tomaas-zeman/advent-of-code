import { Config } from '../..';
import { captcha, parse } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const numbers = parse(data);
  return captcha(numbers, numbers.length / 2);
}

export const testResult = 12;
