class Claim {
  id: number;
  row: number;
  col: number;
  width: number;
  height: number;

  constructor(id: number, row: number, col: number, width: number, height: number) {
    this.id = id;
    this.row = row;
    this.col = col;
    this.width = width;
    this.height = height;
  }

  points(): Point[] {
    const points: Point[] = [];
    for (let row = this.row; row < this.row + this.width; row++) {
      for (let col = this.col; col < this.col + this.height; col++) {
        points.push(new Point(row, col));
      }
    }
    return points;
  }
}

class Point {
  row: number;
  col: number;

  constructor(row: number, col: number) {
    this.row = row;
    this.col = col;
  }

  hash() {
    return `${this.row}x${this.col}`;
  }
}

export function parse(data: string[]): [{ [point: string]: number }, Claim[]] {
  const claims = data.map((line) => {
    // #3 @ 5,5: 2x2
    const match = line.match(/#(\d+) @ (\d+),(\d+): (\d+)x(\d+)/);
    if (!match) {
      throw new Error('Unsupported input data! ' + line);
    }
    const [id, row, col, width, height] = match.slice(1).map((value) => parseInt(value, 10));
    return new Claim(id, row, col, width, height);
  });

  const points: { [point: string]: number } = {};

  for (let claim of claims) {
    for (let point of claim.points()) {
      const key = point.hash();
      if (!points[key]) {
        points[key] = 0;
      }
      points[key]++;
    }
  }

  return [points, claims];
}
