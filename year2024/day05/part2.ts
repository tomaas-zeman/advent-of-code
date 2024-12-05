import { Config } from '../..';
import { sum } from '../../aocutils';
import { parse } from './common';

export async function run(data: string[], config: Config): Promise<string | number> {
  const [rules, updates] = parse(data);

  const fixedUpdates = [];
  for (let update of updates) {
    let wasInvalid = false;
    let isStillInvalid = false;

    while (true) {
      isStillInvalid = false;

      for (let i = 0; i < update.length; i++) {
        const before = update.slice(0, i);
        const number = update[i];
        const after = update.slice(i + 1);

        const shouldBeBefore = rules[number].before.intersection(new Set(after));
        const shouldBeAfter = rules[number].after.intersection(new Set(before));

        if (shouldBeBefore.size || shouldBeAfter.size) {
          wasInvalid = true;
          isStillInvalid = true;

          shouldBeAfter.forEach((value) => before.splice(before.indexOf(value), 1));
          shouldBeBefore.forEach((value) => after.splice(after.indexOf(value), 1));

          update = [
            ...before,
            ...shouldBeBefore.values(),
            number,
            ...shouldBeAfter.values(),
            ...after,
          ];

          break;
        }
      }

      if (!isStillInvalid) {
        break;
      }
    }

    if (wasInvalid) {
      fixedUpdates.push(update);
    }
  }

  return sum(fixedUpdates.map((update) => update[Math.floor(update.length / 2)]));
}

export const testResult = 123;
