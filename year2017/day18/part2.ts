import { Config } from '../..';
import { DefaultMap } from '../../aocutils';
import { Command, Computer, MessageBus } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const bus = new MessageBus(false);
  const computer0 = new Computer(0, new DefaultMap<string, number>(0, [['p', 0]]), bus);
  const computer1 = new Computer(1, new DefaultMap<string, number>(0, [['p', 1]]), bus);

  while (computer0.ip < data.length && computer1.ip < data.length) {
    computer0.processInstruction(...(data[computer0.ip].split(' ') as Command));
    computer1.processInstruction(...(data[computer1.ip].split(' ') as Command));

    if (computer0.waitingForMessage && computer1.waitingForMessage) {
      break;
    }
  }

  return computer1.sentMessages;
}

export const testResult = 3;
