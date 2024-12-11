import { DefaultMap, sum } from '../../aocutils';

export function parse(data: string[]) {
  const stones = data[0].split(' ').asInt();
  return stones.reduce((counts, stone) => {
    counts.set(stone, 1);
    return counts;
  }, new DefaultMap<number, number>(0));
}

function getNewStoneNumbers(stone: number) {
  if (stone === 0) {
    return [1];
  }

  const digits = stone.toString();
  if (digits.length % 2 === 0) {
    return [
      parseInt(digits.substring(0, digits.length / 2)),
      parseInt(digits.substring(digits.length / 2)),
    ];
  }

  return [stone * 2024];
}

export function calculateStonesAfterBlinks(counts: DefaultMap<number, number>, blinks: number) {
  for (let blink = 0; blink < blinks; blink++) {
    const newCounts = new DefaultMap<number, number>(0);
    for (const [number, count] of counts.entries()) {
      for (const newNumber of getNewStoneNumbers(number)) {
        newCounts.set(newNumber, newCounts.get(newNumber) + count);
      }
    }
    counts = newCounts;
  }

  return sum([...counts.values()]);
}
