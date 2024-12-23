import GraphologyGraph from 'graphology';

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
