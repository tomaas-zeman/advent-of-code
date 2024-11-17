import { parse, pickNextStep } from './common';

export function run(data: string[]): string | number {
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
