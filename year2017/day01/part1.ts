import { Config } from '../..';
import { captcha, parse } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const numbers = parse(data);
  return captcha(numbers, 1);
}

export const testResult = 9;
