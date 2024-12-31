import { Config } from '../..';
import { MOVEMENT_CHANGES, parse, Tile } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  let [map, [row, col]] = parse(data);
  let movement = 0;

  while (true) {
    map.set(row, col, Tile.VISITED);

    const nextRow = row + MOVEMENT_CHANGES[movement][0];
    const nextCol = col + MOVEMENT_CHANGES[movement][1];
    if (!map.isInBounds(nextRow, nextCol)) {
      break;
    }

    if (map.get(nextRow, nextCol) === Tile.OBSTACLE) {
      movement = (movement + 1) % 4;
    } else {
      row = nextRow;
      col = nextCol;
    }
  }

  return map.findAll(Tile.VISITED).length;
}

export const testResult = 41;
