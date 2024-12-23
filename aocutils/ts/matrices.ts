import blessed, { Widgets } from 'blessed';
import { Config } from '../..';
import color from 'cli-color';
import { CartesianProduct } from 'js-combinatorics';
import { range } from 'lodash';
import { TypeGuard } from './utils';

export type MatrixAnimationConfig = {
  characterMapping: Record<string, string>;
  colorMapping: Record<string, number>;
  padSize: number;
};

export class MatrixAnimation<T> {
  private matrix: Matrix<T>;
  private config: Config;
  private animationConfig: MatrixAnimationConfig;

  private screen!: Widgets.Screen;
  private box!: Widgets.BoxElement;

  private defaultColorMapping = {
    '#': 26,
    '[': 137,
    ']': 137,
    '.': 232,
    '@': 48,
    '*': 96,
  };

  constructor(
    matrix: Matrix<T>,
    animationConfig?: Partial<MatrixAnimationConfig>,
    config?: Config,
  ) {
    this.matrix = matrix;
    this.config = config ?? ({ visualization: { isEnabled: () => true } } as Config);
    this.animationConfig = {
      colorMapping: this.defaultColorMapping,
      characterMapping: {},
      padSize: 0,
      ...animationConfig,
    };

    if (!this.config.visualization.isEnabled()) {
      return;
    }
    this.screen = blessed.screen({ smartCSR: true });
    this.box = blessed.box();
    this.screen.append(this.box);
    this.screen.key(['escape', 'q', 'C-c'], function () {
      return process.exit(0);
    });
  }

  async render() {
    if (!this.config.visualization.isEnabled()) {
      return;
    }

    let content = this.matrix.toString(
      this.animationConfig.padSize,
      this.animationConfig.colorMapping,
    );
    Object.entries(this.animationConfig.characterMapping).forEach(([oldChar, newChar]) => {
      content = content.replaceAll(oldChar, newChar);
    });

    this.box.setContent(content);
    this.screen.render();
    return new Promise((resolve) => {
      setTimeout(resolve, 0);
    });
  }

  stop() {
    if (!this.config.visualization.isEnabled()) {
      return;
    }
    this.screen.destroy();
  }
}

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
  private neighborChangesOrthogonal = this.neighborChanges.filter(([x, y]) => x === 0 || y === 0);

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

  get(point: [number, number]): T;
  get(row: number, col: number): T;
  get(pointOrRow: [number, number] | number, colOrNothing?: number): T {
    const { row, col } = this.extractParams(pointOrRow, colOrNothing);
    return this.data[row][col];
  }

  set(point: [number, number], value: T): void;
  set(row: number, col: number, value: T): void;
  set(pointOrRow: [number, number] | number, colOrValue: number | T, valueOrNothing?: T) {
    const { row, col, value } = this.extractParams(pointOrRow, colOrValue, valueOrNothing);
    this.data[row][col] = value as T;
  }

  row(row: number): T[] {
    return this.data[row];
  }

  column(col: number): T[] {
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

  neighbors(point: [number, number], includeDiagonal: boolean): T[];
  neighbors(row: number, col: number, includeDiagonal: boolean): T[];
  neighbors(
    pointOrRow: [number, number] | number,
    colOrIncludeDiagonal: number | boolean,
    includeDiagonal = true,
  ): T[] {
    const { row, col } = this.extractParams(pointOrRow, colOrIncludeDiagonal, includeDiagonal);
    return this.neighborPositions(row, col, includeDiagonal).map(
      ([row, col]) => this.data[row][col],
    );
  }

  neighborPositions(point: [number, number], includeDiagonal: boolean): [number, number][];
  neighborPositions(row: number, col: number, includeDiagonal: boolean): [number, number][];
  neighborPositions(
    pointOrRow: [number, number] | number,
    colOrIncludeDiagonal: number | boolean,
    includeDiagonal = true,
  ): [number, number][] {
    const { row, col, value } = this.extractParams(
      pointOrRow,
      colOrIncludeDiagonal,
      includeDiagonal,
    );
    const changes = value ? this.neighborChanges : this.neighborChangesOrthogonal;
    return changes
      .map(([dx, dy]) => {
        const newRow = row + dx;
        const newCol = col + dy;
        return newRow >= 0 && newRow < this.rows && newCol >= 0 && newCol < this.cols
          ? [newRow, newCol]
          : null;
      })
      .filter(Boolean) as [number, number][];
  }

  neighborEntries(point: [number, number], includeDiagonal: boolean): [number, number, T][];
  neighborEntries(row: number, col: number, includeDiagonal: boolean): [number, number, T][];
  neighborEntries(
    pointOrRow: [number, number] | number,
    colOrIncludeDiagonal: number | boolean,
    includeDiagonal = true,
  ): [number, number, T][] {
    const { row, col, value } = this.extractParams(
      pointOrRow,
      colOrIncludeDiagonal,
      includeDiagonal,
    );
    return this.neighborPositions(row, col, !!value).map(([row, col]) => [
      row,
      col,
      this.data[row][col],
    ]);
  }

  find(value: T): [number, number] | null {
    for (const [row, col, val] of this.entries()) {
      if (value === val) {
        return [row, col];
      }
    }
    return null;
  }

  findAll(value: T): [number, number][] {
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

  pad(padSize: number, padValue: T): Matrix<T> {
    const padded = Matrix.create(this.rows + padSize * 2, this.cols + padSize * 2, padValue);
    for (const [row, col, value] of this.entries()) {
      padded.set(row + padSize, col + padSize, value);
    }
    return padded;
  }

  print(padSize = 0, showNumbers = false) {
    console.log(this.toString(padSize, {}, showNumbers), '\n');
  }

  toString(padSize = 0, colorMapping: Record<string, number> = {}, showNumbers = false): string {
    const processChar = (char: T) => {
      const string = typeof char === 'string' ? (char as string) : String(char);
      const padded = string.padStart(padSize, ' ');
      if (string in colorMapping) {
        return color.xterm(colorMapping[string])(padded);
      }
      return padded;
    };
    const header = showNumbers
      ? range(0, this.cols)
          .map((n) => n.toString().padStart(padSize, ' '))
          .join('')
      : '';
    const data = this.data
      .map((row, i) => {
        const rowNumber = showNumbers ? i.toString().padStart(padSize, ' ') : '';
        const rowText = row.map(processChar).join('');
        return `${rowNumber} ${rowText}`;
      })
      .join('\n');
    return `${showNumbers ? ''.padStart(padSize + 1) : ''}${header}\n${data}`;
  }

  /**
   * BEWARE! Use only for small matrices.
   */
  hash(): string {
    return this.data.flatMap((row) => row).join('');
  }

  isInRange(point: [number, number]): boolean;
  isInRange(row: number, col: number): boolean;
  isInRange(pointOrRow: [number, number] | number, colOrNothing?: number): boolean {
    const { row, col } = this.extractParams(pointOrRow, colOrNothing);
    return row >= 0 && row < this.rows && col >= 0 && col < this.cols;
  }

  private extractParams<P>(
    pointOrRow: [number, number] | number,
    colOrValue: number | P,
    value?: P,
  ) {
    if (TypeGuard.isTuple<number>(pointOrRow)) {
      return { row: pointOrRow[0], col: pointOrRow[1], value: colOrValue as P };
    } else if (TypeGuard.isNumber(pointOrRow) && TypeGuard.isNumber(colOrValue)) {
      return { row: pointOrRow, col: colOrValue, value };
    }
    throw new Error('Invalid arguments');
  }
}
