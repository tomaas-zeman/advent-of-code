import { Config } from '../..';
import { computeCheckSum, FS, parse } from './common';

function findSpace(length: number, rightBound: number, fs: FS) {
  for (let i = 0; i < fs.length; i++) {
    let available = true;

    for (let j = 0; j < length; j++) {
      if (fs[i + j] != null || i + j >= rightBound) {
        available = false;
        break;
      }
    }

    if (available) {
      return i;
    }
  }

  return -1;
}

export async function run(data: string[], config: Config): Promise<string | number> {
  let [fs, blockId] = parse(data);
  let right = fs.length - 1;

  while (blockId > 0) {
    const block = [];
    while (fs[right] !== blockId) {
      right--;
    }
    while (fs[right] === blockId) {
      block.push(fs[right]);
      right--;
    }

    const left = findSpace(block.length, right + 1, fs);
    if (left >= 0) {
      const nulls = fs.splice(left, block.length, ...block);
      fs.splice(right + 1, block.length, ...nulls);
    }

    blockId--;
  }

  return computeCheckSum(fs);
}

export const testResult = 2858;
