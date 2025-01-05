import { Config } from '../..';
import { countInfections, State } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const states: State[] = [State.CLEAN, State.WEAKENED, State.INFECTED, State.FLAGGED];
  return countInfections(data, states, 10000000);
}

export const testResult = 2511944;
