import { BaseN } from 'js-combinatorics';
import { DefaultMap, nwise, sum } from '../../aocutils';
import memoize from 'lodash/memoize';

type Mapping = Record<string, Record<string, string>>;
type Paths = DefaultMap<string, Map<string, string[]>>;

const keypadMapping: Mapping = {
  '1': { '^': '4', '>': '2' },
  '2': { '^': '5', '<': '1', '>': '3', v: '0' },
  '3': { '^': '6', '<': '2', v: 'A' },
  '4': { '^': '7', '>': '5', v: '1' },
  '5': { '^': '8', '<': '4', '>': '6', v: '2' },
  '6': { '^': '9', '<': '5', v: '3' },
  '7': { '>': '8', v: '4' },
  '8': { '<': '7', '>': '9', v: '5' },
  '9': { '<': '8', v: '6' },
  '0': { '^': '2', '>': 'A' },
  A: { '^': '3', '<': '0' },
};

const controllerMapping: Mapping = {
  '<': { '>': 'v' },
  v: { '>': '>', '<': '<', '^': '^' },
  '^': { '>': 'A', v: 'v' },
  '>': { '<': 'v', '^': 'A' },
  A: { '<': '^', v: '>' },
};

const keypadSequences = generateAllPaths(keypadMapping);
const controllerSequences = generateAllPaths(controllerMapping);

function findShortestPaths(from: string, to: string, mapping: Mapping): string[] {
  const paths: string[] = [];

  // [current, path from edges, visited nodes]
  const queue: [string, string, string][] = [[from, '', from]];

  while (queue.length > 0) {
    const [current, path, visited] = queue.shift()!;

    if (current === to) {
      paths.push(path + 'A');
      continue;
    }

    for (const [direction, nextNode] of Object.entries(mapping[current])) {
      if (!visited.includes(nextNode)) {
        queue.push([nextNode, path + direction, visited + nextNode]);
      }
    }
  }

  return paths;
}

function generateAllPaths(mapping: Mapping) {
  const paths: Paths = new DefaultMap(() => new Map());
  for (const [from, to] of new BaseN(Object.keys(mapping), 2)) {
    paths.get(from).set(to, findShortestPaths(from, to, mapping));
  }
  return paths;
}

function generateSequences(initialSequence: string, paths: Paths): string[] {
  let sequences: string[] = [];
  let shortestSequence = Number.MAX_SAFE_INTEGER;

  const explore = (sequence: string, from: string, remainingChars: string) => {
    if (remainingChars.length === 0) {
      if (sequence.length === shortestSequence) {
        sequences.push(sequence);
      } else {
        shortestSequence = sequence.length;
        sequences = [sequence];
      }
      return;
    }

    const to = remainingChars[0];

    for (const option of paths.get(from).get(to)!) {
      const nextSequence = sequence + option;
      if (nextSequence.length <= shortestSequence) {
        explore(nextSequence, to, remainingChars.slice(1));
      }
    }
  };

  explore('', 'A', initialSequence);

  return sequences;
}

const calculateControllerSequences = memoize(
  (sequence: string, depth: number) => {
    const pairs = () => nwise(`A${sequence}`.split('')) as [string, string][];
    const nextSequence = (pair: [string, string]) => controllerSequences.get(pair[0]).get(pair[1])!;

    if (depth === 1) {
      return sum(pairs().map((pair) => nextSequence(pair)[0].length));
    }

    let length = 0;

    for (const pair of pairs()) {
      length += Math.min(
        ...nextSequence(pair).map((seq) => calculateControllerSequences(seq, depth - 1)),
      );
    }

    return length;
  },
  (...args) => JSON.stringify(args),
);

export function computeComplexities(data: string[], depth: number) {
  let sumOfComplexities = 0;

  for (const number of data) {
    const initialSequences = generateSequences(number, keypadSequences);
    const bestPath = Math.min(
      ...initialSequences.map((seq) => calculateControllerSequences(seq, depth)),
    );
    sumOfComplexities += bestPath * parseInt(number.replaceAll(/[^\d]/g, ''));
  }

  return sumOfComplexities;
}
