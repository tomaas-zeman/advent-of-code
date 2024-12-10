import { Combination } from 'js-combinatorics';
import { Config } from '../..';
import { DefaultMap } from '../../aocutils';

type Antennas = DefaultMap<string, number[][]>;

export function parse(data: string[]): [Antennas, [number, number]] {
  const antennas = new DefaultMap<string, number[][]>(() => []);

  for (let x = 0; x < data.length; x++) {
    for (let y = 0; y < data[0].length; y++) {
      const tile = data[x][y];
      if (tile !== '.') {
        antennas.get(tile).push([x, y]);
      }
    }
  }

  return [antennas, [data.length, data[0].length]];
}

export async function countAntinodes(
  antennas: Antennas,
  areaSize: [number, number],
  multiples: number[],
  config: Config,
) {
  const [width, height] = areaSize;
  const antinodes = new Set();

  const { visualization } = config;
  await visualization.start();
  visualization.sendData({ areaSize, antennas });

  for (const frequency in antennas) {
    for (const pair of new Combination(antennas.get(frequency), 2)) {
      const [[x1, y1], [x2, y2]] = pair;
      const vector = [x2 - x1, y2 - y1];

      for (const multiple of multiples) {
        const options = [
          [x1 - vector[0] * multiple, y1 - vector[1] * multiple],
          [x2 + vector[0] * multiple, y2 + vector[1] * multiple],
        ];
        options.forEach(([x, y]) => {
          if (x >= 0 && x < width && y >= 0 && y < height) {
            visualization.sendData({ antinode: [x, y] });
            antinodes.add(`${x}:${y}`);
          }
        });
      }
    }
  }

  visualization.stop();

  return antinodes.size;
}
