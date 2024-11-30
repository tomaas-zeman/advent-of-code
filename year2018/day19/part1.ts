import { Config } from '../..';
import { Instruction, instructions } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  let registers = [0, 0, 0, 0, 0, 0];
  const program: [Instruction, number, number, number][] = data.slice(1).map((line) => {
    const [instruction, a, b, c] = line.split(' ');
    return [instructions[instruction], parseInt(a), parseInt(b), parseInt(c)];
  });

  let ipRegister = parseInt(data[0].slice(-1));
  let ipValue = 0;

  while (true) {
    registers[ipRegister] = ipValue;

    const [instruction, a, b, c] = program[ipValue];
    registers = instruction.eval(registers, a, b, c);

    ipValue = registers[ipRegister];
    ipValue++;

    if (ipValue >= program.length) {
      break;
    }
  }

  return registers[0];
}

export const testResult = 6;
