import isEqual from 'lodash/isEqual';
import { Config } from '../..';
import { parseInput, Sample } from './common';
import { instructions } from './common';
import { DefaultMap } from '../../aocutils';

export async function run(data: string[], config: Config): Promise<string | number> {
  const [samples, _] = parseInput(data);

  // Sample -> applicable instructions
  const options = new DefaultMap<Sample, number>(0);

  for (let sample of samples) {
    for (let instruction of Object.values(instructions)) {
      const result = instruction.eval(sample.before, sample.a, sample.b, sample.c);
      const expectedResult = sample.after;
      if (isEqual(result, expectedResult)) {
        options.mapItem(sample, (value) => value + 1);
      }
    }
  }

  return [...options.values()].filter((o) => o >= 3).length;
}

export const testResult = 1;
