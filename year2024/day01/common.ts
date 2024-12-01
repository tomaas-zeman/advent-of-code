export function parseInput(data: string[]): [number[], number[]] {
  const list1: number[] = [];
  const list2: number[] = [];
  for (const line of data) {
    const [left, right] = line.split('   ');
    list1.push(parseInt(left));
    list2.push(parseInt(right));
  }
  return [list1, list2];
}
