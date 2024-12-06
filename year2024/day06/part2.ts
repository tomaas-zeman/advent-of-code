import { Config } from '../..';
import { Tile, MOVEMENT_CHANGES, parse } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const [startingMap, startingPosition] = parse(data);

  let goodObstacles = 0;

  for (const [obstacleRow, obstacleCol] of startingMap.positions()) {
    const map = startingMap.clone();

    // Not necessary but it improves performance by 25%
    if (map.get(obstacleRow, obstacleCol) === Tile.OBSTACLE) {
      continue;
    }
    map.set(obstacleRow, obstacleCol, Tile.OBSTACLE);
    
    let [row, col] = startingPosition;
    let movement = 0;
    const moves = new Set();

    while (true) {
      map.set(row, col, Tile.VISITED);

      const nextRow = row + MOVEMENT_CHANGES[movement][0];
      const nextCol = col + MOVEMENT_CHANGES[movement][1];
      if (nextRow < 0 || nextRow >= map.rows || nextCol < 0 || nextCol >= map.cols) {
        break;
      }

      const move = `${row}:${col}->${nextRow},${nextCol}`;
      if (moves.has(move)) {
        goodObstacles++;
        break;
      }
      moves.add(move);

      if (map.get(nextRow, nextCol) === Tile.OBSTACLE) {
        movement = (movement + 1) % 4;
      } else {
        row = nextRow;
        col = nextCol;
      }
    }
  }

  return goodObstacles;
}

export const testResult = 6;
