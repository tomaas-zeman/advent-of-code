import { Config } from '../..';
import { parse } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const [firewall, numberOfLayers] = parse(data);

  // cycle = 2 * (range - 1)
  // for all depths (depth + delay) % cycle !== 0
  for (let delay = 0; delay < 10000000000; delay++) {
    let caught = false;

    for (let depth = 0; depth <= numberOfLayers; depth++) {
      if (firewall.get(depth).scanner === -1) {
        continue;
      }
      if ((delay + depth) % (2 * (firewall.get(depth).range - 1)) === 0) {
        caught = true;
        break;
      }
    }

    if (!caught) {
      return delay;
    }
  }

  throw new Error('Delay too short!');
}

export const testResult = 10;
