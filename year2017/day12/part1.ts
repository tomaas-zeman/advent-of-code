import { Config } from '../..';
import { parse } from './common';
import { connectedComponents } from 'graphology-library/components';

export async function run(data: string[], config: Config): Promise<string | number> {
  const graph = parse(data);
  const comps = connectedComponents(graph.asGraphologyGraph());
  return comps.find((comp) => comp.includes('0'))!.length;
}

export const testResult = 6;
