import { BaseN } from 'js-combinatorics';

type Equation = {
  result: number;
  numbers: number[];
};

type Operator = (a: number, b: number) => number;

export const OperatorsPart1: Operator[] = [
  (a: number, b: number) => a * b,
  (a: number, b: number) => a + b,
];

export const OperatorsPart2: Operator[] = [
  ...OperatorsPart1,
  (a: number, b: number) => parseInt(`${a}${b}`),
];

function parse(data: string[]): Equation[] {
  return data.map((line) => {
    const [result, b] = line.split(': ');
    const numbers = b.split(' ').asInt();
    return { result: parseInt(result), numbers };
  });
}

function calc(numbers: number[], operators: Operator[]) {
  const result = [...numbers];
  for (const operator of operators) {
    const a = result.shift()!;
    const b = result.shift()!;
    result.unshift(operator(a, b));
  }
  return result[0];
}

export function computeCalibrationResult(data: string[], operators: Operator[]) {
  const equations = parse(data);

  let sum = 0;

  for (const equation of equations) {
    const operatorCombinations = new BaseN(operators, equation.numbers.length - 1).toArray();

    for (const operatorCombination of operatorCombinations) {
      const result = calc(equation.numbers, operatorCombination);
      if (result === equation.result) {
        sum += result;
        break;
      }
    }
  }

  return sum;
}
