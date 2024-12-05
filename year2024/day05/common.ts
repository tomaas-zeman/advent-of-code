import { sum } from '../../aocutils';

type Rules = { [key: number]: { before: Set<number>; after: Set<number> } };
type Update = number[];

export function parse(data: string[]): [Rules, Update[]] {
  const rules: Rules = {};
  const updates: Update[] = [];

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

export function sort(update: Update, rules: Rules) {
  return update.toSorted((a, b) => {
    if (rules[a].before.has(b)) {
      return 1;
    } else if (rules[a].after.has(b)) {
      return -1;
    } else {
      return 0;
    }
  });
}

export function calculateResult(data: string[], filter: (a: Update, b: Update) => Boolean): number {
  const [rules, updates] = parse(data);
  const selectedUpdates = updates
    .map((update) => sort(update, rules))
    .filter((sorted, i) => filter(updates[i], sorted));

  return sum(selectedUpdates.map((update) => update[Math.floor(update.length / 2)]));
}
