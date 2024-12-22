import { BaseN } from 'js-combinatorics';
import { DefaultMap } from '../../aocutils';
import range from 'lodash/range';

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

function findShortestPaths(from: string, to: string, mapping: Mapping): string[] {
  const paths: string[] = [];
  const visited = new Set<string>();

  // [current, path from edges, visited nodes]
  const queue: [string, string, string][] = [[from, '', from]];

  while (queue.length > 0) {
    const [current, path, visited] = queue.shift()!;

    if (current === to) {
      paths.push(path);
      continue;
    }

    for (const [direction, nextNode] of Object.entries(mapping[current])) {
      if (!visited.includes(nextNode)) {
        queue.push([nextNode, path + direction, visited + nextNode]);
      }
    }
  }

  const shortestLength = Math.min(...paths.map((p) => p.length));
  return paths.filter((p) => p.length === shortestLength);
}

function generateAllPaths(mapping: Mapping) {
  const paths: Paths = new DefaultMap(() => new Map());
  for (const [from, to] of new BaseN(Object.keys(mapping), 2)) {
    paths.get(from).set(to, findShortestPaths(from, to, mapping));
  }
  return paths;
}

class Module {
  private paths: Paths;
  private current = 'A';

  constructor(paths: Paths) {
    this.paths = paths;
  }

  sequencesFor(initialSequences: string[]): string[] {
    let sequences: string[] = [];
    let shortestSequence = Number.MAX_SAFE_INTEGER;
    
    const cache = new Map<string, number>(); // try caching parts ...A and count them

    const explore = (sequence: string, currentChar: string, remainingChars: string) => {
      if (remainingChars.length === 0) {
        if (sequence.length === shortestSequence) {
          sequences.push(sequence);
        } else {
          shortestSequence = sequence.length;
          sequences = [sequence];
        }
        return;
      }

      const nextChar = remainingChars[0];

      for (const option of this.paths.get(currentChar).get(nextChar)!) {
        const nextSequence = sequence + option + 'A';
        if (nextSequence.length <= shortestSequence) {
          explore(nextSequence, nextChar, remainingChars.slice(1));
        }
      }
    };

    for (const initialSequence of initialSequences) {
      explore('', this.current, initialSequence);
    }

    return sequences;
  }
}

export function computeComplexities(data: string[], controllerRobots: number) {
  const controllerPaths = generateAllPaths(controllerMapping);
  const keypadPaths = generateAllPaths(keypadMapping);

  let sumOfComplexities = 0;

  for (const number of data) {
    const keypadModule = new Module(keypadPaths);
    const controllerModules = range(0, controllerRobots).map(() => new Module(controllerPaths));

    let sequences = keypadModule.sequencesFor([number]);
    for (const module of controllerModules) {
      sequences = module.sequencesFor(sequences);
    }

    sumOfComplexities += sequences[0].length * parseInt(number.replaceAll(/[^\d]/g, ''));
  }

  return sumOfComplexities;
}
