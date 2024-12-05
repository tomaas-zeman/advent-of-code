import { Config } from '../..';
import { sum } from '../../aocutils';
import { parse } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const [rules, updates] = parse(data);

  const validUpdates = [];
  for (const update of updates) {
    let isValid = true;

    for (let i = 0; i < update.length; i++) {
      const before = new Set(update.slice(0, i));
      const number = update[i];
      const after = new Set(update.slice(i + 1));
      if (
        rules[number].before.intersection(after).size ||
        rules[number].after.intersection(before).size
      ) {
        isValid = false;
        break;
      }
    }

    if (isValid) {
      validUpdates.push(update);
    }
  }

  return sum(validUpdates.map((update) => update[Math.floor(update.length / 2)]));
}

export const testResult = 143;
