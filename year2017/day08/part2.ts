import { Config } from '../..';
import { DefaultMap } from '../../aocutils';
import { parse } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const instructions = parse(data);
  const registers = new DefaultMap(0);
  let max = 0;

  for (const i of instructions) {
    if (!i.condition(registers.get(i.conditionRegisterA), i.conditionValueB)) {
      continue;
    }
    registers.mapItem(i.register, (value) => i.operation(value, i.operationValue));
    max = Math.max(max, Math.max(...registers.values()));
  }

  return max;
}

export const testResult = 10;
