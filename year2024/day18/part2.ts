import { Config } from '../..';
import { BisectRange, BisectRangeDirection, dijkstra, Matrix } from '../../aocutils';
import { parse } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const [bytes, [width, height]] = parse(data, config);

  const bisect = new BisectRange(0, width * height);

  while (bisect.hasNext()) {
    const i = bisect.next();
    const memory = Matrix.create(width, height, '.');
    for (const byte of bytes.slice(0, i)) {
      memory.set(byte, '#');
    }
    const distances = dijkstra(memory, [0, 0], ['.']);
    const cost = distances.get([width - 1, height - 1]);
    bisect.setDirection(
      cost === Number.MAX_SAFE_INTEGER ? BisectRangeDirection.LEFT : BisectRangeDirection.RIGHT,
    );
  }

  return bytes[bisect.current].join(',');
}

export const testResult = '6,1';
