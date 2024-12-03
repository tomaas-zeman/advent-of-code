//-------------------
//     MATRICES     -
//-------------------

export type MatrixEntry<T> = [number, number, T];

export class Matrix<T> {
  data: T[][];
  rows: number;
  cols: number;

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
   * Intervals are always [start, end), e.i. unbounded end if provided.
   */
  slice(rowStart: number = 0, rowEnd?: number, colStart: number = 0, colEnd?: number): T[][] {
    rowEnd = rowEnd ?? this.rows;
    colEnd = colEnd ?? this.cols;
    return this.data.slice(rowStart, rowEnd).map((row) => row.slice(colStart, colEnd));
  }

  diagonal(secondary = false) {
    if (this.rows !== this.cols) {
      throw new Error('Only square matrix is supported for diagonal');
    }

    const d: T[] = [];
    if (!secondary) {
      for (let i = 0; i < this.cols; i++) {
        d.push(this.data[i][i]);
      }
    } else {
      for (let i = 0; i < this.cols; i++) {
        d.push(this.data[this.cols - 1 - i][this.cols - 1 - i]);
      }
    }
    return d;
  }

  neighbors(row: number, col: number): T[] {
    return [
      row - 1 >= 0 && col - 1 >= 0 && this.data[row - 1][col - 1],
      row - 1 >= 0 && this.data[row - 1][col],
      row - 1 >= 0 && col + 1 < this.cols && this.data[row - 1][col + 1],
      col - 1 >= 0 && this.data[row][col - 1],
      col + 1 < this.cols && this.data[row][col + 1],
      row + 1 < this.rows && col - 1 >= 0 && this.data[row + 1][col - 1],
      row + 1 < this.rows && this.data[row + 1][col],
      row + 1 < this.rows && col + 1 < this.cols && this.data[row + 1][col + 1],
    ].filter(Boolean) as T[];
  }

  clone(): Matrix<T> {
    return new Matrix(this.data.map((row) => row.slice()));
  }

  print(padSize = 0): void {
    console.log(
      this.data
        .map((row) => row.map((col) => (col as string).padStart(padSize, ' ')).join(''))
        .join('\n'),
      '\n',
    );
  }

  hash(): string {
    return this.data.flatMap((row) => row).join('');
  }
}

//-----------------
//     ARRAYS     -
//-----------------

export function zip<T, U>(arr1: T[], arr2: T[], callback: (a: T, b: T) => U): U[] {
  if (arr1.length !== arr2.length) {
    throw new Error('Arrays must have the same length to zip.');
  }

  const result: U[] = [];
  for (let i = 0; i < arr1.length; i++) {
    result.push(callback(arr1[i], arr2[i]));
  }
  return result;
}

export function sum(arr: number[]): number {
  return arr.reduce((sum, n) => sum + n, 0);
}

export function range(from: number, to: number): number[] {
  const numbers: number[] = [];
  for (let n = from; n < to; n++) {
    numbers.push(n);
  }
  return numbers;
}

export function arraysEqual<T>(arr1: T[], arr2: T[]) {
  if (arr1.length !== arr2.length) {
    return false;
  }
  for (let i = 0; i < arr1.length; i++) {
    if (arr1[i] !== arr2[i]) {
      return false;
    }
  }
  return true;
}

export function groupBy<T, U extends string | number>(arr: T[], groupingFn: (item: T) => U) {
  return arr.reduce(
    (groups, item) => {
      const group = groupingFn(item);
      if (!groups[group]) {
        groups[group] = [];
      }
      groups[group].push(item);
      return groups;
    },
    {} as { [group in U]: T[] },
  );
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

export function counter<T extends string | number>(
  arr: T[],
  condition: (item: T) => boolean = () => true,
) {
  return arr.reduce(
    (counts, x) => {
      if (condition(x)) {
        counts[x] = (counts[x] || 0) + 1;
      }
      return counts;
    },
    {} as { [key in T]: number },
  );
}

// Modulo that produces positive results for negative numbers.
// For example -3 mod 5 = 2
export function mod(number: number, base: number) {
  return ((number % base) + base) % base;
}
