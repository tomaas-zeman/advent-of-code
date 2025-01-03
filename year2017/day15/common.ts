export const factorA = 16807n;
export const factorB = 48271n;
const divisor = 2147483647n;

type Generator = { next: () => bigint };

export function createGenerator(number: bigint, factor: bigint, divisibleBy: bigint): Generator {
  return {
    next: () => {
      number = (number * factor) % divisor;
      while (number % divisibleBy !== 0n) {
        number = (number * factor) % divisor;
      }
      return number;
    },
  };
}

export function countMatches(genA: Generator, genB: Generator, iterations: number) {
  let matches = 0;
  for (let i = 0; i < iterations; i++) {
    if (matchInLastBits(genA.next(), genB.next())) {
      matches++;
    }
  }
  return matches;
}

function matchInLastBits(a: bigint, b: bigint) {
  return a.toString(2).slice(-16) === b.toString(2).slice(-16);
}

export function parse(data: string[]): [bigint, bigint] {
  return data.map((line) => line.match(/(\d+)/)![1]).map((n) => BigInt(n)) as [bigint, bigint];
}
