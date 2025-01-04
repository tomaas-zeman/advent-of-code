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