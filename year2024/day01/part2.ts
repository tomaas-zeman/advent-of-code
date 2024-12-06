import countBy from 'lodash/countBy';
import { Config } from '../..';
import { parseInput } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const [list1, list2] = parseInput(data);
  const list2Counts = countBy(list2);

  const { visualization } = config;
  await visualization.start();
  visualization.sendData({ numbers: list1, counts: list2Counts });
  visualization.stop();

  return list1.reduce((sum, n) => sum + n * (list2Counts[n] || 0), 0);
}

export const testResult = 31;
