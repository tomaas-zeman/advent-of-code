import { rotate } from '../../aocutils';

export function runKnotHash(lengths: number[], numbers: number[], repetitions: number) {
  let position = 0;
  let skipSize = 0;

  for (let i = 0; i < repetitions; i++) {
    for (const length of lengths) {
      rotate(numbers, position);
      const reversedPart = numbers.slice(0, length).reverse();
      numbers.splice(0, reversedPart.length, ...reversedPart);
      rotate(numbers, position, true);

      position = (position + length + skipSize) % numbers.length;
      skipSize++;
    }
  }

  return numbers;
}
