export class Point {
  id: number;
  row: number;
  col: number;

  constructor(id: number, row: number, col: number) {
    this.id = id;
    this.row = row;
    this.col = col;
  }
}

export function parse(data: string[]) {
  return data.map((line, index) => {
    const [col, row] = line.split(', ').map((value) => parseInt(value));
    return new Point(index + 1, row, col);
  });
}

export function manhattan(p1: Point, p2: Point) {
  return Math.abs(p1.row - p2.row) + Math.abs(p1.col - p2.col);
}
