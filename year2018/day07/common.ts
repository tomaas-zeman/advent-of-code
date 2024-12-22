export class Step {
  name: string;
  time: number;
  prev: Step[] = [];
  next: Step[] = [];
  visited: boolean = false;
  workerAssigned: boolean = false;

  constructor(name: string) {
    this.name = name;
    this.time = 60 + name.charCodeAt(0) - "A".charCodeAt(0);
  }
}

function ensureSteps(stepNames: string[], steps: Record<string, Step>) {
  for (let stepName of stepNames) {
    if (!steps[stepName]) {
      steps[stepName] = new Step(stepName);
    }
  }
}

export function parse(data: string[]) {
  const steps: Record<string, Step> = {};

  for (let line of data) {
    const match = line.match(/Step (.) must be finished before step (.) can begin/);
    if (!match) {
      continue;
    }
    const [current, next] = match.slice(1);
    ensureSteps([current, next], steps);

    steps[current].next.push(steps[next]);
    steps[next].prev.push(steps[current]);
  }

  return steps;
}
export function pickNextStep(available: Set<Step>) {
  const sortedByName = [...available.values()].sort(
    (s1, s2) => s1.name.charCodeAt(0) - s2.name.charCodeAt(0),
  );
  return sortedByName.find((step) => step.prev.every((p) => p.visited) && !step.workerAssigned);
}
