import { Matrix, mod } from '../../aocutils';

type Robot = { x: number; y: number; vx: number; vy: number };

export class Lobby {
  tiles: Matrix<number>;

  constructor(rows: number, cols: number, initialRobotPositions: Robot[]) {
    this.tiles = Matrix.create(rows, cols, 0);
    for (const robot of initialRobotPositions) {
      this.tiles.set(robot.y, robot.x, this.tiles.get(robot.y, robot.x) + 1);
    }
  }

  moveRobot(robot: Robot) {
    this.tiles.set(robot.y, robot.x, this.tiles.get(robot.y, robot.x) - 1);
    robot.x = mod(robot.x + robot.vx, this.tiles.cols);
    robot.y = mod(robot.y + robot.vy, this.tiles.rows);
    this.tiles.set(robot.y, robot.x, this.tiles.get(robot.y, robot.x) + 1);
  }
}

export function parse(data: string[], width: number, height: number): [Lobby, Robot[]] {
  const robots = [];

  for (const line of data) {
    const [x, y, vx, vy] = line.matchAll(/(-?\d+)/g).map((m) => parseInt(m[1]));
    robots.push({ x, y, vx, vy });
  }

  return [new Lobby(height, width, robots), robots];
}
