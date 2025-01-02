import { Config } from '../..';
import { parse } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const [firewall, numberOfLayers] = parse(data);

  let me = -1;
  let severity = 0;

  for (let step = 0; step <= numberOfLayers; step++) {
    me++;

    for (let depth = 0; depth <= numberOfLayers; depth++) {
      const { scanner, range } = firewall.get(depth);
      if (me === depth && scanner === 0) {
        severity += depth * range;
      }
      if (scanner >= 0) {
        firewall.mapItem(depth, ({ range, scanner, direction }) => {
          if (scanner === range - 1 && direction === 'down') {
            direction = 'up';
          }
          if (scanner === 0 && direction === 'up') {
            direction = 'down';
          }
          return { range, direction, scanner: scanner + (direction === 'up' ? -1 : 1) };
        });
      }
    }
  }

  return severity;
}

export const testResult = 24;
