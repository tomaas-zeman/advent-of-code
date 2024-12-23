import Graph from 'graphology';
import { Config } from '../..';
import { parse } from './common';

export function findMaximumCliques(graph: Graph) {
  const cliques: string[][] = [];

  // Finding sets of nodes in a graph connected to each other is a 'clique' problem
  // https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
  //
  // algorithm BronKerbosch1(R, P, X) is
  //   if P and X are both empty then
  //       report R as a maximal clique
  //   for each vertex v in P do
  //       BronKerbosch1(R ⋃ {v}, P ⋂ N(v), X ⋂ N(v))
  //       P := P \ {v}
  //       X := X ⋃ {v}
  function bronKerbosch(R: string[], P: string[], X: string[]) {
    if (P.length === 0 && X.length === 0) {
      cliques.push(R);
      return;
    }

    for (const node of P) {
      const neighbors = graph.neighbors(node);

      bronKerbosch(
        [...R, node],
        P.filter((n) => neighbors.includes(n)),
        X.filter((n) => neighbors.includes(n)),
      );

      P.splice(P.indexOf(node), 1);
      X.push(node);
    }
  }

  bronKerbosch([], graph.nodes(), []);

  return cliques;
}

export async function run(data: string[], config: Config): Promise<string | number> {
  const graph = parse(data);
  const cliques = findMaximumCliques(graph);
  return cliques
    .sort((a, b) => b.length - a.length)[0]
    .sort()
    .join(',');
}

export const testResult = 'co,de,ka,ta';
