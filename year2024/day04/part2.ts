import { Config } from '../..';
import { Matrix } from '../../aocutils';

const WORD_LENGTH = 3;

function isValid(word: string) {
  return ['SAM', 'MAS'].includes(word);
}

export async function run(data: string[], config: Config): Promise<string | number> {
  const board = new Matrix(data.map((line) => line.split('')));
  let count = 0;

  for (let row = 0; row <= board.rows - WORD_LENGTH; row++) {
    for (let col = 0; col <= board.cols - WORD_LENGTH; col++) {
      const slice = new Matrix(board.slice(row, row + WORD_LENGTH, col, col + WORD_LENGTH));
      const primary = slice.diagonal().join('');
      const secondary = slice.diagonal(true).join('');
      if (isValid(primary) && isValid(secondary)) {
        count++;
      }
    }
  }

  return count;
}

export const testResult = 9;
