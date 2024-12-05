type Rules = { [key: number]: { before: Set<number>; after: Set<number> } };
type Updates = number[][];

export function parse(data: string[]): [Rules, Updates] {
  const rules: Rules = {};
  const updates: Updates = [];

  function add(x: number, y: number) {
    if (!rules[x]) {
      rules[x] = { before: new Set(), after: new Set() };
    }
    if (!rules[y]) {
      rules[y] = { before: new Set(), after: new Set() };
    }
    rules[x].after.add(y);
    rules[y].before.add(x);
  }

  for (const line of data) {
    if (line.includes('|')) {
      const [x, y] = line.split('|').map((v) => parseInt(v));
      add(x, y);
    } else if (line.includes(',')) {
      updates.push(line.split(',').map((v) => parseInt(v)));
    }
  }

  return [rules, updates];
}
