import { Config } from '../..';
import { sum } from '../../aocutils';
import { parse } from './common';
import chunk from 'lodash/chunk';
import { Worker } from 'worker_threads';

const WORKER_THREADS = 10;

export async function run(data: string[], config: Config): Promise<string | number> {
  if (config.isTest) {
    return '';
  }

  const [startingMap, startingPosition] = parse(data);

  const workers: Promise<number>[] = [];
  const chunks = chunk(
    [...startingMap.positions()],
    (startingMap.cols * startingMap.cols) / WORKER_THREADS,
  );

  for (const positions of chunks) {
    const workerData = { startingMap, positions, startingPosition };
    workers.push(
      new Promise((resolve) => {
        const worker = new Worker('./year2024/day06/worker.js', { workerData });
        worker.on('message', resolve);
      }),
    );
  }

  return sum(await Promise.all(workers));
}

export const testResult = '';
