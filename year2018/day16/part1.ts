import isEqual from 'lodash/isEqual';
import { Config } from '../..';
import { parseInput, Sample } from './common';
import { instructions } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const [samples, _] = parseInput(data);

  // Sample -> applicable instructions
  const options = new Map<Sample, number>();

  for (let sample of samples) {
    for (let instruction of Object.values(instructions)) {
      const result = instruction.eval(sample.before, sample.a, sample.b, sample.c);
      const expectedResult = sample.after;
      if (isEqual(result, expectedResult)) {
        options.set(sample, (options.get(sample) ?? 0) + 1);
      }
    }
  }

  return [...options.values()].filter((o) => o >= 3).length;
}

export const testResult = 1;
