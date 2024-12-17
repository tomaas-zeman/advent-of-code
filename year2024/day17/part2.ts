import isEqual from 'lodash/isEqual';
import { Config } from '../..';
import { Computer, parse, Registers } from './common';

function isInvalidNumber(program: number[], output: number[]) {
  if (output.length > program.length) {
    return true;
  }
  for (let i = 0; i < output.length; i++) {
    if (output[i] !== program[i]) {
      return true;
    }
  }
  return false;
}

export async function run(data: string[], config: Config): Promise<string | number> {
  const [registers, program] = parse(data);

  for (let value = 0; value < Number.MAX_SAFE_INTEGER; value++) {
    const comp = new Computer([BigInt(value), ...registers.slice(1)] as Registers);

    while (comp.ip < program.length) {
      const opcode = program[comp.ip];
      const operand = program[comp.ip + 1];
      comp.process(opcode, operand);

      if (isInvalidNumber(program, comp.output)) {
        break;
      }

      if (isEqual(program, comp.output)) {
        return value;
      }

      // TODO: try to see if certain numbers create a loop -> skip them
    }
  }

  throw new Error('Solution not found!');
}

export const testResult = 117440;
