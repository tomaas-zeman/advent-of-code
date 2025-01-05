import { Config } from '../..';
import { Command, Computer } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  if (config.isTest) {
    return 0;
  }

  const computer = new Computer();

  while (computer.ip < data.length) {
    const [instruction, register, value] = data[computer.ip].split(' ') as Command;
    computer.processInstruction(instruction, register, value);
  }

  return computer.mulCount;
}

export const testResult = 0;
