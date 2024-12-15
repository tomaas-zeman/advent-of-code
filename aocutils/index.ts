import { CartesianProduct } from 'js-combinatorics';
import blessed, { Widgets } from 'blessed';
import color from 'cli-color';
import GraphologyGraph from 'graphology';
// import { renderToPNG } from 'graphology-canvas/node';
// import forceLayout from 'graphology-layout-force';
import { Config } from '..';

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

  get(row: number, col: number): T {
    return this.data[row][col];
  }

  set(row: number, col: number, value: T) {
    this.data[row][col] = value;
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

  neighbors(row: number, col: number, includeDiagonal = true): T[] {
    return this.neighborPositions(row, col, includeDiagonal).map(
      ([row, col]) => this.data[row][col],
    );
  }

  neighborPositions(row: number, col: number, includeDiagonal = true): [number, number][] {
    const changes = includeDiagonal ? this.neighborChanges : this.neighborChangesOrthogonal;
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

  print(padSize = 0) {
    console.log(this.toString(padSize), '\n');
  }

  toString(padSize = 0, colorMapping: { [char: string]: number } = {}): string {
    const processChar = (char: T) => {
      const string = typeof char === 'string' ? (char as string) : String(char);
      const padded = string.padStart(padSize, ' ');
      if (string in colorMapping) {
        return color.xterm(colorMapping[string])(padded);
      }
      return padded;
    };
    return this.data.map((row) => row.map(processChar).join('')).join('\n');
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

export type PriorityQueueItem<T> = { priority: number } & T;

export class PriorityQueue<T> {
  private queue: PriorityQueueItem<T>[] = [];

  constructor(initialItems: PriorityQueueItem<T>[] = []) {
    initialItems.forEach((item) => this.enqueue(item));
  }

  enqueue(item: PriorityQueueItem<T>) {
    if (this.size() === 0) {
      this.queue.push(item);
      return;
    }

    for (let i = 0; i < this.queue.length; i++) {
      if (item.priority < this.queue[i].priority) {
        this.queue.splice(i, 0, item);
        return;
      }
    }

    this.queue.push(item);
  }

  dequeue() {
    return this.queue.shift();
  }

  peek(): PriorityQueueItem<T> | undefined {
    return this.queue[0];
  }

  size() {
    return this.queue.length;
  }
}

//---------------
//     MAPS     -
//---------------

type DefaultValue<T> = T | (() => T);

export class DefaultMap<K, V> extends Map<K, V> {
  private defaultValue: DefaultValue<V>;

  constructor(defaultValue: DefaultValue<V>, iterable?: Iterable<[K, V]>) {
    super(iterable);
    this.defaultValue = defaultValue;
  }

  private getDefaultValue() {
    return isFunction(this.defaultValue) ? this.defaultValue() : this.defaultValue;
  }

  get(key: K): V {
    let value = super.get(key);
    if (value === undefined) {
      value = this.getDefaultValue();
      super.set(key, value);
    }
    return value;
  }

  mapItem(key: K, mappingFn: (value: V) => V) {
    this.set(key, mappingFn(this.get(key)));
  }
}

//---------------
//     SETS     -
//---------------

export class HashSet<T> extends Set {
  constructor(initialItems: Iterable<T> = []) {
    super();
    for (const item of initialItems) {
      this.add(item);
    }
  }

  add(value: T) {
    return super.add(JSON.stringify(value));
  }

  has(value: T) {
    return super.has(JSON.stringify(value));
  }

  delete(value: T) {
    return super.delete(JSON.stringify(value));
  }

  *values(): SetIterator<T> {
    for (const item of super.values()) {
      yield JSON.parse(item);
    }
  }
}

//-----------------
//     GRAPHS     -
//-----------------

export class Graph {
  private directed: boolean;

  private nodes: string[] = [];
  private edges: [string, string, number][] = [];

  constructor(directed = false) {
    this.directed = directed;
  }

  addNode(node: string) {
    this.nodes.push(node);
  }

  addEdge(source: string, target: string, weight: number = 0) {
    this.edges.push([source, target, weight]);
  }

  asGraphologyGraph() {
    const graph = new GraphologyGraph({
      multi: true,
      type: this.directed ? 'directed' : 'undirected',
    });
    this.nodes.forEach((node) => graph.addNode(node));
    this.edges.forEach(([source, target, weight]) => graph.addEdge(source, target, { weight }));
    return graph;
  }

  // draw() {
  //   const graph = this.asGraphologyGraph();
  //   forceLayout.assign(graph, 50);
  //   renderToPNG(graph, 'graph.png', {}, () => {});
  // }
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
  Array.prototype.get = function (index: number) {
    if (index >= 0) {
      return this[index];
    }
    return this[this.length + index];
  };
}

export function isFunction(variable: any): variable is Function {
  return typeof variable === 'function';
}

export type MatrixAnimationConfig = {
  characterMapping: { [char: string]: string };
  colorMapping: { [char: string]: number };
};

export class MatrixAnimation<T> {
  private matrix: Matrix<T>;
  private config: Config;
  private animationConfig: MatrixAnimationConfig;

  private screen!: Widgets.Screen;
  private box!: Widgets.BoxElement;

  constructor(matrix: Matrix<T>, config: Config, animationConfig: MatrixAnimationConfig) {
    this.matrix = matrix;
    this.config = config;
    this.animationConfig = animationConfig;

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

    let content = this.matrix.toString(0, this.animationConfig.colorMapping);
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
