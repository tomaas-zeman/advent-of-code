import { Config } from '../..';
import { Lobby, parse } from './common';

function calculateClustering(lobby: Lobby) {
  let rating = 0;

  for (const row of lobby.tiles.data) {
    let longestRowSequence = 0;
    let currentSequence = 0;

    for (const col of row) {
      if (col > 0) {
        currentSequence++;
      } else {
        longestRowSequence = Math.max(longestRowSequence, currentSequence);
        currentSequence = 0;
      }
    }

    rating += longestRowSequence;
  }

  return rating;
}

export async function run(data: string[], config: Config): Promise<string | number> {
  if (config.isTest) {
    return 0;
  }

  const { visualization } = config;
  await visualization.start();

  const [width, height] = [101, 103];
  const [lobby, robots] = parse(data, width, height);
  const result = { step: 0, clustering: 0 };

  for (let step = 0; step < 10000; step++) {
    for (const robot of robots) {
      lobby.moveRobot(robot);
    }

    visualization.sendData({ robots });

    const clustering = calculateClustering(lobby);
    if (clustering > result.clustering) {
      result.clustering = clustering;
      result.step = step;
    }
  }

  visualization.sendData({ width, height, step: result.step });
  visualization.stop();

  return result.step + 1;
}

export const testResult = 0;
