import { parse, pickNextStep, Step } from './common';

export function run(data: string[], isTest?: boolean): string | number {
  const steps = parse(data);
  const available = new Set(Object.values(steps));
  const workers: (Step | undefined)[] = new Array(isTest ? 2 : 5);

  let seconds = 0;

  while (true) {
    for (let i = 0; i < workers.length; i++) {
      const step = workers[i];
      if (step) {
        if (step.time === 0) {
          step.visited = true;
          workers[i] = pickNextStep(available);
        }
        step.time--;
      } else {
        workers[i] = pickNextStep(available);
      }
      
      const nextStep = workers[i];
      if (nextStep && !nextStep.workerAssigned) {
        nextStep.workerAssigned = true;
      }
    }

    if (workers.every((w) => !w)) {
      break;
    }
    
    seconds++;
  }

  return seconds;
}

export const testResult = 258;
