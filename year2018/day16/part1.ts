import { Config } from '../..';
import { arraysEqual } from '../../aocutils';
import { parseInput } from './common';
import { instructions } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const [samples, _] = parseInput(data);

  // Sample ID -> applicable instructions
  const options: { [sampleId: number]: number } = samples.reduce((acc, sample) => {
    acc[sample.id] = 0;
    return acc;
  }, {});

  for (let sample of samples) {
    for (let instruction of Object.values(instructions)) {
      const result = instruction.eval(sample.before, sample.a, sample.b, sample.c);
      const expectedResult = sample.after;
      if (arraysEqual(result, expectedResult)) {
        options[sample.id]++;
      }
    }
  }

  return Object.values(options).filter((o) => o >= 3).length;
}

export const testResult = 1;
