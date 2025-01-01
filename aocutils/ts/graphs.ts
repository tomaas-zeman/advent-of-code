import GraphologyGraph from 'graphology';
import { isEqual } from './utils';

//-----------------
//     GRAPHS     -
//-----------------

export class Graph {
  private directed: boolean;

  private nodes: Set<string> = new Set();
  private edges: [string, string, number][] = [];

  constructor(directed = false) {
    this.directed = directed;
  }

  addNode(node: string) {
    this.nodes.add(node);
  }

  addEdge(source: string, target: string, weight: number = 0) {
    for (const node of [source, target]) {
      this.addNode(node);
    }

    // Do not add the same/opposite edge for undirected graphs again
    if (
      !this.directed &&
      this.edges.find(
        (e) => isEqual(e, [source, target, weight]) || isEqual(e, [target, source, weight]),
      )
    ) {
      return;
    }

    this.edges.push([source, target, weight]);
  }

  asGraphologyGraph() {
    const graph = new GraphologyGraph({
      multi: this.directed,
      type: this.directed ? 'directed' : 'undirected',
    });
    this.nodes.forEach((node) => graph.addNode(node));
    this.edges.forEach(([source, target, weight]) => graph.addEdge(source, target, { weight }));
    return graph;
  }
}
