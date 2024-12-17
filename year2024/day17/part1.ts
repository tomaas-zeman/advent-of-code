import { Config } from '../..';
import { Computer, parse } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const [registers, program] = parse(data);
  const comp = new Computer(registers);

  while (comp.ip < program.length) {
    const opcode = program[comp.ip];
    const operand = program[comp.ip + 1];
    comp.process(opcode, operand);
  }

  return comp.output.join(',');
}

export const testResult = '4,6,3,5,6,3,5,2,1,0';
