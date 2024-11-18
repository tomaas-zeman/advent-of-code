import { Config } from '../..';
import { parse, pickNextStep } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const steps = parse(data);
  const available = new Set(Object.values(steps));

  let seq = '';
  while (true) {
    const step = pickNextStep(available);
    if (!step) {
      break;
    }
    step.visited = true;
    available.delete(step);
    seq += step.name;
  }

  return seq;
}

export const testResult = 'CABDFE';
