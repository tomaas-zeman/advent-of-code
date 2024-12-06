import { Config } from '../..';

type Point = {
  position: [number, number];
  velocity: [number, number];
};

export function parse(data: string[]): Point[] {
  // position=<-3,  6> velocity=< 2, -1>
  return data.map((line) => {
    const [px, py, vx, vy] = line
      .match(/position=< *(-?\d+), *(-?\d+)> velocity=< *(-?\d+), *(-?\d+)>/)!
      .slice(1)
      .asInt();
    return { position: [px, py], velocity: [vx, vy] };
  });
}

export async function run(data: string[], config: Config): Promise<string | number> {
  const points = parse(data);

  // Use visualization to see the result
  await config.visualization.start();
  points.forEach((point) => config.visualization.sendData({ point }));
  config.visualization.stop();

  return 0;
}

export const testResult = 0;
