import { Config } from '../..';
import { sum } from '../../aocutils';
import { parse } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const width = config.isTest ? 11 : 101;
  const height = config.isTest ? 7 : 103;

  const [lobby, robots] = parse(data, width, height);

  for (let step = 0; step < 100; step++) {
    for (const robot of robots) {
      lobby.moveRobot(robot);
    }
  }

  const quadrants = [
    lobby.tiles.slice(0, Math.floor(height / 2), 0, Math.floor(width / 2)),
    lobby.tiles.slice(0, Math.floor(height / 2), Math.ceil(width / 2), width),
    lobby.tiles.slice(Math.ceil(height / 2), height, 0, Math.floor(width / 2)),
    lobby.tiles.slice(Math.ceil(height / 2), height, Math.ceil(width / 2), width),
  ];

  return quadrants.map((q) => q.flatMap((v) => v)).reduce((prod, q) => prod * sum(q), 1);
}

export const testResult = 12;
