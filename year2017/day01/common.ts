import { mod } from '../../aocutils';

export function parse(data: string[]) {
  return data[0].split('').asInt();
}

export function captcha(numbers: number[], offset: number) {
  let sum = 0;
  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] === numbers[mod(i + offset, numbers.length)]) {
      sum += numbers[i];
    }
  }
  return sum;
}
