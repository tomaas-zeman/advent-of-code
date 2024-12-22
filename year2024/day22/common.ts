export const STEPS = 2000;

function randomize(number: number) {
  const mask = (1 << 24) - 1;
  number = ((number << 6) ^ number) & mask;
  number = ((number >> 5) ^ number) & mask;
  number = ((number << 11) ^ number) & mask;
  return number;
}

export function getSecretNumbers(seed: number) {
  const numbers = [seed];
  for (let step = 0; step < STEPS; step++) {
    numbers.push(randomize(numbers[step]));
  }
  return numbers;
}
