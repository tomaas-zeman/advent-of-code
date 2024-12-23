import { Config } from '../..';
import { HashSet } from '../../aocutils';
import { parse } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const graph = parse(data);

  const tripplets = new HashSet<string[]>();

  for (const node of graph.nodes()) {
    graph.neighbors(node).forEach((node2) => {
      for (const node3 of graph.nodes()) {
        if (node3 === node || node3 === node2) {
          continue;
        }
        const neighbors = graph.neighbors(node3);
        if (neighbors.includes(node) && neighbors.includes(node2)) {
          tripplets.add([node, node2, node3].sort());
        }
      }
    });
  }

  return [...tripplets.values().filter((t) => t.some((value) => value.startsWith('t')))].length;
}

export const testResult = 7;
