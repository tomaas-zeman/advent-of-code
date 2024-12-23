import GraphologyGraph from 'graphology';
import { Matrix } from './matrices';
import { DefaultMap, HashSet, PriorityQueue } from './collections';

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

export type Node = [number, number];
export type Distances = DefaultMap<Node, number>;
export type State = { priority: number; point: Node };

export function dijkstra<T>(matrix: Matrix<T>, start: Node, visitableNodes: T[]): Distances {
  const distances: Distances = new DefaultMap(Number.MAX_SAFE_INTEGER, [], true);
  const nodes = matrix.entries().filter(([_, __, value]) => visitableNodes.includes(value));
  for (const [row, col] of nodes) {
    distances.set([row, col], row === start[0] && col === start[1] ? 0 : Number.MAX_SAFE_INTEGER);
  }

  const visited = new HashSet<Node>();

  const queue = new PriorityQueue<State>([{ priority: 0, point: start }]);
  while (queue.size() > 0) {
    const { point: current } = queue.dequeue()!;

    visited.add(current);

    const neighbors = matrix
      .neighborPositions(current, false)
      .filter((node) => !visited.has(node) && visitableNodes.includes(matrix.get(node)));

    for (const next of neighbors) {
      const newDistance = distances.get(current) + 1;

      if (newDistance < distances.get(next)) {
        distances.set(next, newDistance);
        queue.enqueue({ priority: newDistance, point: next });
      }
    }
  }

  return distances;
}
