import { Config } from '../..';
import { DefaultMap } from '../../aocutils';
import { parse } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const instructions = parse(data);
  const registers = new DefaultMap(0);

  for (const i of instructions) {
    if (!i.condition(registers.get(i.conditionRegisterA), i.conditionValueB)) {
      continue;
    }
    registers.mapItem(i.register, (value) => i.operation(value, i.operationValue));
  }

  return Math.max(...registers.values());
}

export const testResult = 1;
