export type Point = {
  id: number;
  row: number;
  col: number;
};

export function parse(data: string[]): Point[] {
  return data.map((line, index) => {
    const [col, row] = line.split(', ').asInt();
    return { id: index + 1, row, col };
  });
}

export function manhattan(p1: Point, p2: Point) {
  return Math.abs(p1.row - p2.row) + Math.abs(p1.col - p2.col);
}
