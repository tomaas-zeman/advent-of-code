import { CartesianProduct } from 'js-combinatorics';

//-------------------
//     MATRICES     -
//-------------------

export type MatrixEntry<T> = [number, number, T];

export class Matrix<T> {
  data: T[][];
  rows: number;
  cols: number;

  private neighborChanges = new CartesianProduct([-1, 0, 1], [-1, 0, 1])
    .toArray()
    .filter(([x, y]) => x !== 0 || y !== 0);

  constructor(data: T[][]) {
    this.data = data;
    this.rows = data.length;
    this.cols = data[0].length;
  }

  static create<T>(numRows: number, numCols: number, defaultValue: T): Matrix<T> {
    const rows: T[][] = [];
    for (let row = 0; row < numRows; row++) {
      const cols: T[] = [];
      for (let col = 0; col < numCols; col++) {
        cols.push(defaultValue);
      }
      rows.push(cols);
    }
    return new Matrix(rows);
  }

  *positions(): Generator<[number, number]> {
    for (let row = 0; row < this.rows; row++) {
      for (let col = 0; col < this.cols; col++) {
        yield [row, col];
      }
    }
  }

  *entries(): Generator<[number, number, T]> {
    for (const [row, col] of this.positions()) {
      yield [row, col, this.data[row][col]];
    }
  }

  *values(): Generator<T> {
    for (const [row, col] of this.positions()) {
      yield this.data[row][col];
    }
  }

  get(row: number, col: number): T {
    return this.data[row][col];
  }

  set(row: number, col: number, value: T) {
    this.data[row][col] = value;
  }

  getRow(row: number): T[] {
    return this.data[row];
  }

  getColumn(col: number): T[] {
    const data: T[] = [];
    for (let row = 0; row < this.rows; row++) {
      data.push(this.data[row][col]);
    }
    return data;
  }

  /**
   * Slice the matrix.
   *
   * Intervals are always [start, end), e.i. unbounded.
   */
  slice(rowStart: number, rowEnd: number, colStart: number, colEnd: number): T[][] {
    return this.data.slice(rowStart, rowEnd).map((row) => row.slice(colStart, colEnd));
  }

  diagonal(secondary = false) {
    if (this.rows !== this.cols) {
      throw new Error('Only square matrix is supported for diagonal');
    }

    const items: T[] = [];
    if (!secondary) {
      for (let i = 0; i < this.cols; i++) {
        items.push(this.data[i][i]);
      }
    } else {
      for (let i = 0; i < this.cols; i++) {
        items.push(this.data[this.cols - 1 - i][i]);
      }
    }
    return items;
  }

  neighbors(row: number, col: number): T[] {
    return this.neighborChanges
      .map(([dx, dy]) => {
        const newRow = row + dx;
        const newCol = col + dy;
        return newRow >= 0 && newRow < this.rows && newCol >= 0 && newCol < this.cols
          ? this.data[newRow][newCol]
          : null;
      })
      .filter(Boolean) as T[];
  }

  search(value: T): [number, number] | null {
    for (const [row, col, val] of this.entries()) {
      if (value === val) {
        return [row, col];
      }
    }
    return null;
  }

  searchAll(value: T): [number, number][] {
    const positions: [number, number][] = [];
    for (const [row, col, val] of this.entries()) {
      if (value === val) {
        positions.push([row, col]);
      }
    }
    return positions;
  }

  clone(): Matrix<T> {
    return new Matrix(this.data.map((row) => row.slice()));
  }

  print(padSize = 0): void {
    const pad = (value: T) =>
      (typeof value === 'string' ? (value as String) : String(value)).padStart(padSize, ' ');
    console.log(this.data.map((row) => row.map(pad).join('')).join('\n'), '\n');
  }

  /**
   * BEWARE! Use only for small matrices.
   */
  hash(): string {
    return this.data.flatMap((row) => row).join('');
  }
}

//-----------------
//     ARRAYS     -
//-----------------

export function sum(arr: number[]): number {
  return arr.reduce((sum, n) => sum + n, 0);
}

export function pairwise<T>(arr: T[], length = 2): T[][] {
  const pairs: T[][] = [];
  for (let i = 0; i < arr.length - (length - 1); i++) {
    pairs.push(arr.slice(i, i + length));
  }
  return pairs;
}

//--------------------
//     UTILITIES     -
//--------------------

// Modulo that produces positive results for negative numbers.
// For example -3 mod 5 = 2
export function mod(number: number, base: number) {
  return ((number % base) + base) % base;
}

export function loadPolyfills() {
  Array.prototype.asInt = function () {
    return this.map((value) => parseInt(value));
  };
}