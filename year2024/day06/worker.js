import { parentPort, workerData } from 'worker_threads';

const Tile = {
  OBSTACLE: '#',
  VISITED: 'X',
};

const MOVEMENT_CHANGES = [
  [-1, 0],
  [0, 1],
  [1, 0],
  [0, -1],
];

const { startingMap, positions, startingPosition } = workerData;

let goodObstacles = 0;

for (const [obstacleRow, obstacleCol] of positions) {
  const map = startingMap.data.map((row) => row.slice());
  map[obstacleRow][obstacleCol] = Tile.OBSTACLE;

  let [row, col] = startingPosition;
  let movement = 0;
  const moves = new Set();

  while (true) {
    map[row][col] = Tile.VISITED;

    const nextRow = row + MOVEMENT_CHANGES[movement][0];
    const nextCol = col + MOVEMENT_CHANGES[movement][1];
    if (nextRow < 0 || nextRow >= map.length || nextCol < 0 || nextCol >= map[0].length) {
      break;
    }

    const move = `${row}:${col}->${nextRow}:${nextCol}`;
    if (moves.has(move)) {
      goodObstacles++;
      break;
    }
    moves.add(move);

    if (map[nextRow][nextCol] === Tile.OBSTACLE) {
      movement = (movement + 1) % 4;
    } else {
      row = nextRow;
      col = nextCol;
    }
  }
}

parentPort.postMessage(goodObstacles);
