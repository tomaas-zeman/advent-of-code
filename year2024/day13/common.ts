export type Machine = number[]; // ax, ay, bx, by, x, y

function parse(data: string[], modifier: number) {
  const machines: Machine[] = [];
  for (let i = 0; i < data.length; i++) {
    const matches = data.slice(i, i + 3).join('').matchAll(/(\d+)/g);
    machines.push([...matches].map((m, i) => parseInt(m[1]) + (i > 3 ? modifier : 0)));
    i += 3;
  }
  return machines;
}

export function calculateCost(data: string[], modifier: number) {
  const machines = parse(data, modifier);

  let cost = 0;
  for (let [ax, ay, bx, by, x, y] of machines) {
    const b = (x * ay - y * ax) / (bx * ay - by * ax);
    const a = (x - b * bx) / ax;
    if (b % 1 === 0 && a % 1 === 0) {
      cost += 3 * a + b;
    }
  }

  return cost.toString();
}
