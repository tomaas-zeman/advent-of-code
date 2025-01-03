import { Config } from '../..';
import { DefaultMap } from '../../aocutils';
import { Command, Computer, Instruction, MessageBus } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const bus = new MessageBus(true);
  const computer = new Computer(0, new DefaultMap<string, number>(0), bus);

  while (computer.ip < data.length) {
    const [instruction, register, value] = data[computer.ip].split(' ') as Command;
    if (instruction === 'rcv') {
      return bus.getNewestMessage(computer.id)!;
    }
    computer.processInstruction(instruction, register, value);
  }

  throw new Error('Should not happen!');
}

export const testResult = 4;
