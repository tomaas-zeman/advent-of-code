import { Config } from '../..';
import { countConnectedComponents } from 'graphology-library/components';
import { parse } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const graph = parse(data);
  return countConnectedComponents(graph.asGraphologyGraph());
}

export const testResult = 2;
