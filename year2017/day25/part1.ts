import { Config } from '../..';

type Option = { write: number; slotChange: number; nextState: string };
type State = [Option, Option];

function parse(data: string[]): [number, Map<string, State>] {
  const extractNumber = (s: string) => parseInt(s.match(/(\d+)/)![0]);
  const extractState = (s: string) => s.match(/state ([A-Z])/)![1];
  const extractSlotChange = (s: string) => (s.includes('to the right') ? 1 : -1);

  const steps = extractNumber(data[1]);
  const states = new Map<string, State>();

  for (let i = 3; i < data.length; i += 10) {
    const state = [0, 4].map((offset) => ({
      write: extractNumber(data[i + 2 + offset]),
      slotChange: extractSlotChange(data[i + 3 + offset]),
      nextState: extractState(data[i + 4 + offset]),
    })) as State;
    states.set(extractState(data[i]), state);
  }

  return [steps, states];
}

export async function run(data: string[], config: Config): Promise<string | number> {
  const [steps, states] = parse(data);

  const tape = [0];
  let index = 0;
  let state = 'A';

  for (let step = 0; step < steps; step++) {
    const option = states.get(state)![tape[index]];

    // adjust tape
    if (index === 0 && option.slotChange < 0) {
      index++;
      tape.unshift(0);
    }
    if (index === tape.length - 1 && option.slotChange > 0) {
      tape.push(0);
    }

    tape[index] = option.write;
    index += option.slotChange;
    state = option.nextState;
  }

  return tape.filter((v) => v === 1).length;
}

export const testResult = 3;
