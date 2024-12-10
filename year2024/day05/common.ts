import { DefaultMap, sum } from '../../aocutils';

type Rule = { before: Set<number>; after: Set<number> };
type Rules = DefaultMap<number, Rule>;
type Update = number[];

export function parse(data: string[]): [Rules, Update[]] {
  const rules = new DefaultMap<number, Rule>(() => ({ before: new Set(), after: new Set() }));
  const updates: Update[] = [];

  for (const line of data) {
    if (line.includes('|')) {
      const [x, y] = line.split('|').asInt();
      rules.get(x).after.add(y);
      rules.get(y).before.add(x);
    } else if (line.includes(',')) {
      updates.push(line.split(',').asInt());
    }
  }

  return [rules, updates];
}

export function sort(update: Update, rules: Rules) {
  return update.toSorted((a, b) => {
    if (rules.get(a).before.has(b)) {
      return 1;
    } else if (rules.get(a).after.has(b)) {
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
