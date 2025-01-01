import range from 'lodash/range';
import { Config } from '../..';
import { runKnotHash } from './common';

function computeDenseHash(numbers: number[]) {
  const denseHash = [];

  for (let i = 0; i < 16; i++) {
    const sliceHash = numbers.slice(i * 16, i * 16 + 16).reduce((a, b) => a ^ b);
    denseHash.push(sliceHash);
  }

  return denseHash.map((n) => n.toString(16).padStart(2, '0')).join('');
}

export async function run(data: string[], config: Config): Promise<string | number> {
  const lengths = [...data[0].split('').map((c) => c.charCodeAt(0)), 17, 31, 73, 47, 23];
  const numbers = range(0, 256);

  runKnotHash(lengths, numbers, 64);
  return computeDenseHash(numbers);
}

export const testResult = '33efeb34ea91902bb2f59c9920caa6cd';
