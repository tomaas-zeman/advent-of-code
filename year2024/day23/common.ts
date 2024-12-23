import GraphologyGraph from 'graphology';
import { Graph } from '../../aocutils';

export function parse(data: string[]): GraphologyGraph {
  const graph = new Graph();
  for (const [a, b] of data.map((line) => line.split('-'))) {
    graph.addEdge(a, b);
  }
  return graph.asGraphologyGraph();
}
