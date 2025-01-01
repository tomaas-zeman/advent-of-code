import { Graph } from '../../aocutils';

export function parse(data: string[]) {
  const graph = new Graph();

  for (const line of data) {
    const [source, targets] = line.split(' <-> ');
    for (const target of targets.split(', ')) {
      graph.addEdge(source, target);
    }
  }

  return graph;
}
