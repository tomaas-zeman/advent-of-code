import { DefaultMap } from '../../aocutils';

function findMemoryBlock(blocks: number[]) {
  let highest = 0;
  let highestIndex = 0;

  for (let i = 0; i < blocks.length; i++) {
    if (blocks[i] > highest) {
      highestIndex = i;
      highest = blocks[i];
    }
  }

  return highestIndex;
}

export function redistribute(data: string[]): [number, number[], DefaultMap<number[], number>] {
  const blocks = data[0].split('\t').asInt();
  const states = new DefaultMap<number[], number>(0, true);

  let steps = 0;
  while (!states.has(blocks)) {
    states.set(blocks, steps);

    let index = findMemoryBlock(blocks);
    let blocksRemaining = blocks[index];
    blocks[index] = 0;
    while (blocksRemaining > 0) {
      index = (index + 1) % blocks.length;
      blocks[index]++;
      blocksRemaining--;
    }

    steps++;
  }

  return [steps, blocks, states];
}
