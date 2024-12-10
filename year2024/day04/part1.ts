import { Config } from '../..';
import { Matrix, pairwise } from '../../aocutils';

const WORD_LENGTH = 4;

function countValid(...words: string[][]) {
  return words.map((w) => w.join('')).filter((w) => ['XMAS', 'SAMX'].includes(w)).length;
}

export async function run(data: string[], config: Config): Promise<string | number> {
  const board = new Matrix(data.map((line) => line.split('')));
  let count = 0;

  // Rows
  for (let row = 0; row < board.rows; row++) {
    count += countValid(...pairwise(board.row(row), WORD_LENGTH));
  }

  // Columns
  for (let col = 0; col < board.cols; col++) {
    count += countValid(...pairwise(board.column(col), WORD_LENGTH));
  }

  // Diagonals
  for (let row = 0; row <= board.rows - WORD_LENGTH; row++) {
    for (let col = 0; col <= board.cols - WORD_LENGTH; col++) {
      const slice = new Matrix(board.slice(row, row + WORD_LENGTH, col, col + WORD_LENGTH));
      count += countValid(slice.diagonal(), slice.diagonal(true));
    }
  }

  return count;
}

export const testResult = 18;
