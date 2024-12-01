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

  entries() {
    const entries: MatrixEntry<T>[] = [];
    for (let row = 0; row < this.rows; row++) {
      for (let col = 0; col < this.cols; col++) {
        entries.push([row, col, this.data[row][col]]);
      }
    }
    return entries;
  }

  get(row: number, col: number): T {
    return this.data[row][col];
  }

  set(row: number, col: number, value: T) {
    this.data[row][col] = value;
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

export function counter<T extends string | number>(arr: T[]) {
  return arr.reduce(
    (counts, x) => {
      counts[x] = (counts[x] || 0) + 1;
      return counts;
    },
    {} as { [key in T]: number },
  );
}
