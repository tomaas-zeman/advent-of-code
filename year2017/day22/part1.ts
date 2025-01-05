import { Config } from '../..';
import { countInfections, State } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const states: State[] = [State.CLEAN, State.INFECTED];
  return countInfections(data, states, 10000);
}

export const testResult = 5587;
