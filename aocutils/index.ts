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
