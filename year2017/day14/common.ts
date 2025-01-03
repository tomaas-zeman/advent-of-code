import range from 'lodash/range';
import { Config } from '../..';
import { run as knotHash } from '../day10/part2';
import { Matrix } from '../../aocutils';

function hexToBin(hex: string) {
  let bin = '';
  for (const char of hex) {
    bin += parseInt(char, 16).toString(2).padStart(4, '0');
  }
  return bin;
}

export async function createDisk(data: string[], config: Config) {
  const hashes = await Promise.all(
    range(0, 128).map((i) => knotHash([`${data[0]}-${i}`], config) as Promise<string>),
  );
  return new Matrix<string>(hashes.map(hexToBin).map((row) => row.split('')));
}
